# $REDACTED — Launch Runbook

Privacy meta rider. ZEC wave (ZEC $20B, ZCAT $43M, MASK $25M, Sapling +82%). Document aesthetic unclaimed. Ticker attempts exist but all dead (top $36K FDV) — consolidation play.

---

## 1. Account setup (do this first, 24–48h before token)

**X account**
- Handle options (check availability): `@RedactedDossier` / `@TheRedactedFile` / `@RedactedIntel` / `@RedactedOnSol`
- Display name: `REDACTED` (or `████████`)
- Bio: `SOURCE: ████████. CONFIDENCE: ████████.`
- PFP: dossier folder with black bars (see art brief)
- Banner: redacted document strip, "CLASSIFIED // EYES ONLY" stamp
- No link in bio pre-launch. That's the point.

**Telegram** (optional, create day-of): `t.me/RedactedDossier`

---

## 2. Art brief (one image, one banner — keep it cheap)

**PFP (1000×1000):**
- Manila / off-white document card on dark background
- Header text: `DOSSIER #001` in small monospace
- Three to four thick black censor bars where "fields" would be
- One red rubber stamp: `CLASSIFIED` (rotated slightly)
- Bottom corner: tiny `$REDACTED`
- Font: IBM Plex Mono or Courier. No logos, no faces, no animals.
- *Alternative concept:* suited figure silhouette, eyes replaced by one black bar. Same stamp.

**Banner (1500×500):**
- Repeat pattern of redacted lines, one line fully readable in red: `PRIVACY IS NOT A FEATURE. IT'S A RIGHT.`
- Dark background, scan-line texture optional

Free tools: Figma free tier, Canva free, or any image model. Do not overthink — the meme is the format, not the art.

---

## 3. Pre-launch posts (first 10 — no token, no link)

Post 1–2 per day over 48–72h. Never mention a coin. Never mention buying anything.

1. `SOURCE: ████████. CONFIDENCE: ████████. ACTION: NONE.`
2. `The cat took the mask. The mask took the sapling.`
   `The document is still on the desk.`
3. `ZEC: ████████. That's not a glitch. That's the point.`
4. `[FILE 001 — PARTIAL DECLASSIFICATION]`
   `Everyone is watching the shielded pool.`
   `Nobody is reading the file.`
5. `Privacy memecoins so far:`
   `- Cat: $43M`
   `- Mask: $25M`
   `- Document: ████████`
6. `IF YOU CAN READ THIS, YOU ARE ALREADY IN THE FILE.`
7. `STATUS UPDATE:`
   `Narrative: LIVE`
   `Mascot: ████████`
   `Clearance: PENDING`
8. `A cat is cute. A mask is edgy.`
   `A redacted file is a threat.`
9. `We are not building a product.`
   `We are renting a wave.`
   `The wave is called privacy.`
   `The surfboard is a document.`
10. (Launch day, 2–4h before token) `DECRYPT THIS:`
    `The file opens at [TIME] UTC.`
    `Contract: ████████`
    `Clearance: PUBLIC`

Reply under real ZEC/privacy news with redacted versions of headlines once you have ~300+ followers. Do not spam.

---

## 4. Launch mechanics (pump.fun)

1. Fund a **fresh wallet** with ~0.2–0.5 SOL (launch fee + first buys + rent). Fresh = no prior token history.
2. Go to pump.fun, connect wallet.
3. Name: `REDACTED` — Symbol: `REDACTED` (or `████████` if the name field allows Unicode; test in preview).
4. Description: `SOURCE: ████████. CONFIDENCE: ████████. Privacy is the wave. This is the document. 0/0. No team. No promises. The only product is the meme.`
5. Image: dossier PFP.
6. Website field: **your deployed site URL** (see §5).
7. Launch, then **immediately**:
   - Pin a tweet: contract address + site link + pump.fun link. Only ever verify CA via this pinned tweet.
   - Drop into the acquisition channel of your choice (you're on your own for KOL/CT posting — post the pinned link under the launch tweet itself).
   - Buy a small amount yourself if you want the curve to look alive (your choice; disclose nothing, break no rules — you're just a holder).
8. After graduation (~$69K mcap bonding curve): the site auto-embeds the DexScreener chart once you paste the CA into `index.html`. Redeploy or edit the one config line.

**Hard rules (repeat):**
- No fake Elon/ZEC-team/partnership posts.
- No wash trading rings.
- No "guaranteed", "100x", "soon listing on Binance" language.
- One lie ends the dossier permanently.

---

## 5. Website — Cloudflare Pages (chosen host, free)

Site is `/Users/mac/redacted/` — `index.html` + `pfp.png` + `banner.png` + `og.png` (single-file site, zero dependencies).

**One-time account setup (use the new Gmail):**
1. Go to https://dash.cloudflare.com/sign-up
2. Sign up with **redacted.tokenomics@gmail.com** — verify the email
3. No payment method needed for Pages free tier

**Deploy:**
1. dash.cloudflare.com → **Workers & Pages** → **Create** → **Pages** tab → **Upload assets**
2. Project name: `redacted` (this gives you **redacted.pages.dev** if the name is free; if taken try `redacted-intel`, `reddcted`, `redacted-dossier`)
3. Drag the entire `/Users/mac/redacted` folder (or select it)
4. Deploy → live at `https://redacted.pages.dev` with SSL, free forever, unlimited bandwidth

**After token launch, edit these lines in `index.html` and re-deploy** (Workers & Pages → your project → Create deployment → drag folder again):
```
const CONTRACT_ADDRESS = "YOUR_CA_HERE";
const X_URL            = "https://x.com/YOURHANDLE";
const TELEGRAM_URL     = "https://t.me/YOURCHANNEL";
```
That single edit turns the site live: buy button activates, CA displays, DexScreener chart embeds, X/Telegram links connect.

**Assets included:**
- `pfp.png` (1000×1000) — dossier PFP for X + pump.fun upload
- `banner.png` (1500×500) — X header banner
- `og.png` (1200×630) — link-preview image (auto-wired via meta tags)
- `generate_assets.py` — regenerate/modify the art anytime (`python3 generate_assets.py`)

---

## 6. Timeline summary

| When | Action |
|---|---|
| T-72h | Create X account + art + deploy teaser site (no CA config) |
| T-72h to T-24h | Posts 1–9, engage under ZEC tweets, grow to a few hundred follows |
| T-4h | Post 10 (declassify teaser), confirm site live, fund launch wallet |
| T-0 | Launch on pump.fun, pin CA tweet, swap site config, redeploy |
| T+0 to T+24h | Reply with redacted content under every privacy headline; monitor; do not panic-sell the narrative |
| Post-graduation | Chart live on site; consider a "FILE 002" content drop |

---

## 7. Risk notes (read once, internalize)

- This is a **trade on attention**, not a company. Wave can die in 48h. Size accordingly — money you can lose entirely.
- ZEC itself dumping ~0.6% today is normal; the meta is still hot (Sapling +82%).
- Ticker attempts exist ($36K top, dead). Ours wins via execution + timing, not novelty of the word.
- You are renting the ZEC wave — if ZEC rolls over hard, the rider rolls too. No product backing.
- Nothing here is financial advice. You are launching a joke with a chart attached.

---

## 8. File checklist

- [x] `/Users/mac/redacted/index.html` — live site (single file + assets)
- [x] `pfp.png` / `banner.png` / `og.png` — brand assets generated
- [ ] Cloudflare account created (redacted.tokenomics@gmail.com)
- [ ] Pages project `redacted` deployed → redacted.pages.dev
- [ ] X account created (PFP + banner uploaded)
- [ ] Posts 1–9 scheduled/posted
- [ ] Launch wallet funded
- [ ] pump.fun launch (site URL + pfp.png in listing)
- [ ] CA pasted into `index.html`, Pages re-deployed
- [ ] Pinned CA tweet live
