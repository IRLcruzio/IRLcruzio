// Usage:
//   node render.js preview 3,10,18      -> writes preview PNGs at the given seconds
//   node render.js video out.mp4 audio.wav
const { chromium } = require('playwright');
const { spawn } = require('child_process');
const path = require('path');
const fs = require('fs');

(async () => {
  const [mode, a1, a2] = process.argv.slice(2);
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
  page.on('pageerror', e => console.error('PAGE ERROR', e.message));
  await page.goto('file://' + path.join(__dirname, 'scene.html'));
  await page.evaluate(() => document.fonts.ready);
  await page.evaluate(async () => { for (const f of ['900 10px "Inter Display"', '800 10px "Inter"', '700 10px "JetBrains Mono"', 'italic 500 10px "Inter"']) await document.fonts.load(f); });

  if (mode === 'preview') {
    const out = a2 || __dirname;
    for (const s of a1.split(',').map(Number)) {
      const url = await page.evaluate(t => window.frame(t), s);
      fs.writeFileSync(path.join(out, `prev_${String(s).padStart(5, '0')}.jpg`), Buffer.from(url.split(',')[1], 'base64'));
    }
  } else {
    const fps = 30; const dur = await page.evaluate(() => window.DURATION);
    const ff = spawn('ffmpeg', ['-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', String(fps), '-c:v', 'mjpeg', '-i', '-',
      '-i', a2, '-c:v', 'libx264', '-preset', 'medium', '-crf', '20', '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '192k',
      '-shortest', '-movflags', '+faststart', a1], { stdio: ['pipe', 'inherit', 'inherit'] });
    const total = Math.round(dur * fps);
    for (let i = 0; i < total; i++) {
      const url = await page.evaluate(t => window.frame(t), i / fps);
      const buf = Buffer.from(url.split(',')[1], 'base64');
      if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
      if (i % 300 === 0) console.log(`frame ${i}/${total}`);
    }
    ff.stdin.end();
    await new Promise(r => ff.on('close', r));
  }
  await browser.close();
})();
