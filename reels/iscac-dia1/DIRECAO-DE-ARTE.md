# ISCAC · "DIA 1" — Faltam 5 dias para CF I

**Formato:** 9:16 (1080×1920), 30 fps, **45 s**
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

### Só o João no ecrã
- **Uma única mesa** (a do João) e **nenhuma outra pessoa**: o Aquário está vazio de madrugada, o que reforça a solidão e o desespero.
- **A mesa é o caos:** folhas espalhadas (multiplicam-se depois do time-lapse), **torre de cafés** que cresce de 6 para 10 copos até bater no candeeiro, calculadora, lata de energético, livro "CF I" e o **calendário colado no vidro: "EXAME CF I – FALTAM 5 DIAS"**.
- **O João** tem cabeça grande, traço grosso e expressões exageradas: **olheiras roxas sempre**, suor, olhos que mudam (confuso, arregalado, a cair de sono, a implorar, determinado) e tremores.

---

## 2. Pacing (45 s)

| Tempo | Cena | O que acontece | Truque de retenção |
|---|---|---|---|
| 0.0–3.0 | **Hook** | Grande plano: o João olha para "Balanço e Demonstração de Resultados", aparecem "???" | Texto do hook logo aos 0,3 s |
| 3.0–4.6 | Reveal | **Zoom out** com "whoosh": ele está sozinho no Aquário, às 02:47 | Primeira quebra de padrão aos 3 s |
| 4.6–9.0 | **Plano de Contas** | Balão de pensamento com **slot machine**: "Conta 22 = ?" → a roleta abranda e para em "CAFÉ ☕" → ✗ "(era Fornecedores...)" | O plano geral, antes parado, passa a ter uma piada |
| 9.0–11.3 | Caneta | "SEM TINTA?!" | Corte a cada 2–3 s até aos 29 s |
| 11.3–13.8 | T de Razão | DÉBITO e CRÉDITO trocam de lugar → carimbo **ERRADO** | |
| 13.8–17.0 | **IVA** | Exercício "1 000 € + IVA (23%)": tecla a tecla, faz **1000 × 23 = 23 000** → "IVA = 23 000 €?!" → a calculadora rebenta (ERR, fumo) → correção a vermelho: "IVA = 230 € (não 23 000!)" | Piada de nicho: quem estuda CF I comenta |
| 17.0–20.2 | **Balanço** | Balança: ATIVO 12 500,00 € vs PASSIVO + CP 12 499,99 € (−0,01 €). Ele põe um café no prato para "equilibrar" → **O BALANÇO NÃO BATE!** | |
| 20.2–23.4 | **Inventários** | Caixas FIFO (LOTE 1 a 4). Ele tira o de cima (LOTE 4) → **LIFO?! PROIBIDO NO SNC** (NCRF 18) → a pilha cai | Erro clássico de exame |
| 23.4–26.4 | **Time-lapse** | ▶▶ x60. O relógio passa de 02:47 para 04:12, a torre de cafés cresce, as folhas multiplicam-se e muda de pose a cada 0,33 s. Barra **ENERGIA DO JOÃO** com "Depreciação: −20%/h (quotas constantes)" | Muda o ritmo e mostra o tempo a passar |
| 26.4–29.3 | Café | "GLUP GLUP" → "CAFEÍNA 300%" → adormece e cai | |
| 29.3–31.9 | **PUM!** | Cara esborrachada no vidro, "*squeeeak*" | Frame mais partilhável |
| 31.9–37.0 | Pedido | "*plop*". A marca da cara fica no vidro. Olha para a câmara e implora, com trombone triste | Quebra da 4.ª parede |
| 37.0–38.0 | **Revelação** | Ecrã escurece, alarme, fita "CF I" na cabeça, "LEVEL UP!" | Mudança de cor e de ritmo |
| 38.0–42.6 | HUD | Painel com Like, Comentário e Repost. Ele aponta para cada regra e "Quantos lançamentos ele faz hoje?" | Regras só no fim, como pedido |
| 42.6–45.0 | **Follow** | "SEGUE para veres se ele sobrevive ao DIA 2 →" | CTA para seguir, para a série ter continuidade |

**Som:** batida lo-fi com tic-tac de relógio até ao "PUM!" (hi-hats a dobrar no time-lapse). Cada gag tem o seu efeito: roleta, teclas da calculadora com explosão, pancada da balança, caixas a cair, fita a acelerar. Depois silêncio, chiado no vidro e trombone triste. No HUD, alarme, arpejo de "level up" e uma batida rápida de 128 bpm até ao fim.

### Exercícios de CF I usados
O repositório **Vault** não tinha exercícios: só um README e um ficheiro com texto aleatório. Por isso usei exercícios típicos de CF I com o SNC: plano de contas (11, 12, 21, 22, 24, 31, 62, 71), compra a crédito com IVA a 23% (D 31 / D 2432 / C 221), equação do Balanço (Ativo = Passivo + Capital Próprio), inventários FIFO vs LIFO (NCRF 18) e depreciações em quotas constantes. Se puseres os teus exercícios no Vault, posso trocar os números e enunciados pelos teus.

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
