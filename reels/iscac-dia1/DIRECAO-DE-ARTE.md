# ISCAC · "DIA 1" — Faltam 5 dias para CF I

**Formato:** 9:16 (1080×1920), 30 fps, **30 s**
**Ficheiros:**
- `iscac-dia1.mp4`: vídeo final animado, com som
- `cena4.html`: frame-chave da Cena 4 em HTML/CSS + SVG, num único ficheiro e animado. Abre-se no browser.
- `capa.jpg`: capa (frame do HUD)
- `src/`: código que gera o vídeo (`scene.html` para a imagem, `audio.py` para o som, `render.js` para o MP4)

---

## 1. Direção de arte: da foto real ao 2D minimalista

### O que mantive das fotos (a identidade do "Aquário")
| Elemento real (fotos) | Como ficou em 2D | Porquê |
|---|---|---|
| **Parede de vidro** de alto a baixo, com caixilhos metálicos verticais e uma travessa horizontal | A câmara está **sempre do lado de fora do vidro**, no corredor. Caixilhos cinza-escuros nas laterais, travessa a meio, reflexos diagonais suaves e um tom azulado no vidro | É o que torna o espaço um "aquário": quem passa no corredor vê lá dentro. É a piada visual do sítio. |
| **Candeeiros lineares** em barra metálica, presos em postes nas mesas, com luz branca-quente por baixo | Barra metálica com uma linha emissiva por baixo e um cone de luz em degradê sobre a mesa do João | É o detalhe mais reconhecível das mesas do ISCAC |
| **Candeeiros pendentes em sino** junto às janelas altas | Três sinos com halo quente nas janelas superiores | Dão profundidade e marcam o pé-direito alto |
| **Cadeiras bordô** e **mesas de madeira clara** | Paleta fixa: bordô `#6d1a26` e madeira `#d8b98c` | São as cores do espaço. Mesmo em stickman, reconhece-se logo |
| **Paredes de betão** | Degradê castanho-acinzentado com juntas verticais e pequenas manchas | Textura do betão, mas simplificada |
| **Corredor exterior** escuro, com chão reflexivo e grelha metálica junto ao vidro | Faixa inferior escura com grelha listrada e reflexos quentes das luzes de dentro | É exatamente o enquadramento da foto noturna |
| **Letreiro vermelho ISCAC** (foto 1) | Néon vermelho estilizado (arco + "ISCAC") com brilho e uma falha ocasional | Situa a cena no ISCAC sem precisar de explicar. *Se tiverem o logótipo oficial e autorização para o usar, é só substituir.* |

### A noite
- **Contraste quente/frio:** interior âmbar (luz dos candeeiros) e exterior azul-escuro e roxo (céu nas janelas altas, reflexos no corredor). É a paleta da foto noturna que enviaste.
- **Relógio digital vermelho a marcar 02:47:** diz logo que é madrugada antes do exame, sem precisar de texto.
- **Vinheta e grão de filme leve:** dão o tom "cinematográfico" pedido para os primeiros 25 s.

### O contraste cómico
- **À volta está tudo calmo:** 4 colegas em stickman pequeno, simples, a pestanejar devagar (um de headphones a abanar a cabeça, outros no portátil ou a ler).
- **A mesa do João é o caos:** folhas espalhadas, **torre de 6→7 copos de café** a abanar, calculadora, lata de energético, livro "CF I" e o **calendário colado no vidro: "EXAME CF I – FALTAM 5 DIAS"**.
- **O João** tem cabeça grande, traço grosso e expressões exageradas: **olheiras roxas sempre**, suor a escorrer, olhos que mudam (confuso, arregalado, a cair de sono, a implorar com lágrimas, determinado) e tremores.

---

## 2. Pacing (retenção)

| Tempo | Cena | O que acontece | Truque de retenção |
|---|---|---|---|
| 0.0–3.0 | **1 · Hook** | Grande plano: o João olha para "Balanço e Demonstração de Resultados", pestaneja, aparecem "???" | O texto do hook aparece **logo aos 0,3 s** (estilo "sticker" de TikTok) |
| 3.0–3.6 | 1 · Reveal | **Zoom out rápido** com "whoosh": afinal está no Aquário, de noite | Primeira quebra de padrão aos 3 s |
| 3.6–10 | 1 · Contexto | Plano geral: os colegas calmos contra o caos do João, calendário "5 DIAS", relógio 02:47 | O espectador tem tempo para "ler" as piadas visuais |
| 10–12.3 | **2 · Montagem** | Inserto: a caneta **não escreve** → "SEM TINTA?!" | Corte a cada ~2–2,5 s |
| 12.3–14.8 | 2 | T de Razão: "DÉBITO" e "CRÉDITO" **trocam de lugar**, escreve "100 €" do lado errado → carimbo **ERRADO** + buzzer | Piada de nicho: quem estuda Contabilidade identifica-se |
| 14.8–15.9 | 2 | Café de penálti: "GLUP GLUP" | |
| 15.9–16.9 | 2 | "CAFEÍNA 300%": olhos arregalados, tremores, raios | |
| 16.9–17.7 | 2 | Os olhos fecham e cai de cara para a câmara | Tensão física antes do impacto |
| 17.7–20.3 | 2 · Clímax cómico | **"PUM!"**: cara esborrachada contra o vidro, mãos abertas, bafo no vidro, "*squeeeak*" a escorregar | O frame mais "printável" e partilhável |
| 20.3–25 | **3 · Pedido** | "*plop*": descola-se. Fica a marca da cara no vidro. Olha para a câmara (4.ª parede), mãos juntas, lágrimas, trombone triste | Empatia e quebra da 4.ª parede preparam o CTA |
| 25–25.8 | **4 · Revelação** | Ecrã escurece, alarme, a **fita "CF I" cai na cabeça** | Mudança de cor e de ritmo: "agora é a sério" |
| 25.8–30 | 4 · HUD | **"LEVEL UP!"**, painel de regras com Like, Comentário e Repost. O João aponta freneticamente para cada regra, que acende à vez. CTA a amarelo | As regras só aparecem nos últimos ~4 s, como pedido |

**Som:** batida lo-fi com tic-tac de relógio até ao "PUM!". Depois silêncio, chiado no vidro e trombone triste. No HUD, alarme, arpejo de "level up" e uma batida rápida de 128 bpm até ao fim.

---

## 3. Mecânicas (só nos últimos segundos)
- 👍 **LIKE** = +1 Lançamento Contabilístico (Débito/Crédito)
- 💬 **COMENTÁRIO** = +1 Diário Completo do Caderno
- 🔄 **REPOST** = +1 Hora de Estudo Teórico

O HUD tem "DIA 1 / 5" e um contador "LANÇAMENTOS: ???" a piscar. No episódio do "DIA 2" podem pôr lá o número real de likes do Dia 1.

---

## 4. Prompt para gerar o próximo dia

```
Cria o reel "DIA 2" da série ISCAC (faltam 4 dias para CF I), com o mesmo estilo e o
mesmo código de reels/iscac-dia1/src (Aquário do ISCAC à noite, vista do corredor através
do vidro, João em stickman com olheiras, mesa caótica, legendas em "sticker" branco).
30 s, 1080x1920. O Dia 1 teve [X] likes, [Y] comentários e [Z] reposts: o João tem de
fazer exatamente X lançamentos, Y diários e Z horas de teoria, e o vídeo mostra-o a
tentar (com falhas cómicas). Calendário no vidro: "FALTAM 4 DIAS". HUD só nos últimos
5 s com as mesmas regras e o contador atualizado.
```
