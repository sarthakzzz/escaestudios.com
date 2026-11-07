#!/usr/bin/env python3
"""Writes the inner pages of escaestudios.com with the shared header and footer."""
from pathlib import Path

HERE = Path(__file__).resolve().parent
NAV = [("./", "Home"), ("plugins.html", "Plugins"), ("about.html", "About"), ("support.html", "Support")]


def page(fname, title, desc, body):
    cur = ' aria-current="page"'
    nav = "\n".join(
        f'      <li><a href="{h}"{cur if h == fname else ""}>{t}</a></li>' for h, t in NAV
    )
    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} · Escae Studios</title>
<meta name="description" content="{desc}">
<link rel="icon" href="img/orange-crusher.jpg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600;9..144,800&family=Nunito:wght@400;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css">
</head>
<body>
<header class="topbar">
  <div class="wrap">
    <a class="brand" href="./">Escae <span>Studios</span></a>
    <nav aria-label="Main"><ul>
{nav}
    </ul></nav>
  </div>
</header>

<main>
{body}
</main>

<footer>
  <div class="wrap">
    <p>© 2026 Escae Studios. All rights reserved.<br>Contact: <a href="mailto:hello@escaestudios.com">hello@escaestudios.com</a></p>
    <ul>
      <li><a href="about.html">About</a></li>
      <li><a href="support.html">Support</a></li>
      <li><a href="privacy.html">Privacy</a></li>
      <li><a href="terms.html">Terms</a></li>
    </ul>
  </div>
</footer>
</body>
</html>
"""
    (HERE / fname).write_text(html)


PLUGINS = [
    ("orange-crusher", "Distortion", "Orange Crusher", "Juicy distortion, squeezed fresh. From gentle warmth to full fuzz."),
    ("butter-spread", "Free", "Butter Spread", "A stereo widener that spreads your sound while keeping the bass solid in mono."),
    ("popping-candy", "Stutter &amp; slicer", "Popping Candy", "Tempo-synced stutters, slices and arps that fizz."),
    ("spice-shelf", "EQ", "Spice Shelf EQ", "An equaliser where every spice jar seasons a different part of the spectrum."),
    ("popcorn-sandwich", "Compressor", "Popcorn Sandwich", "One knob: squeeze it tight, or make it pop as an expander."),
    ("spaghetti-delay", "Delay", "Spaghetti Delay", "Tempo-synced echoes that twirl, tangle and saturate."),
    ("bread-oven", "Reverb", "Bread Oven Reverb", "Warm algorithmic space, from a small room to a huge hall."),
    ("cherry-on-the-top", "Mastering", "Cherry on the Top", "One-dial mastering chain for the finishing touch."),
    ("food-fight", "Multi-effect", "Food Fight", "A chaotic multi-effect that throws everything at your sound."),
    ("ghost-pepper", "Clipper", "Ghost Pepper Clipper", "Hot, clean loudness with soft and hard clipping."),
    ("hot-o-pan", "Auto-pan", "Hot-o-Pan", "Moves your sound from side to side, in time with the track."),
    ("gummy-gate", "Gate", "Gummy Gate", "Noise gate and rhythmic gate patterns, chewy and bouncy."),
    ("milkshake-chorus", "Chorus", "Milkshake Chorus", "Thick, swirly, smooth chorus and ensemble."),
    ("burnt-toast", "Tape", "Burnt Toast", "Tape-machine warmth with wow, flutter and saturation."),
    ("noodle-filter", "Filter", "Noodle Filter", "Resonant filters that wiggle in tempo-synced steps."),
    ("muesli-granular", "Granular", "Muesli Granular", "A granular effect that scatters your audio into tiny grains."),
]

items = "\n".join(
    f'      <article class="item"><img src="img/{s}.jpg" alt="{n} artwork" loading="lazy">'
    f'<span class="tag{" free" if t == "Free" else ""}">{t}</span><h3>{n}</h3><p>{d}</p></article>'
    for s, t, n, d in PLUGINS
)

page("plugins.html", "Plugins", "The Plugins for Breakfast range by Escae Studios: sixteen AU and VST3 audio effect plugins for macOS.", f"""  <section class="hero page-title wrap">
    <span class="badge">Plugins for Breakfast</span>
    <h1>Sixteen plugins on the <span>menu</span></h1>
    <p class="lede">Every plugin is an AU and VST3 audio effect for macOS, drawn as a little felt world you can play with. Available from 1 December 2026.</p>
  </section>
  <section class="wrap">
    <div class="menu">
{items}
    </div>
  </section>
  <section class="wrap">
    <div class="split">
      <img src="img/full-fridge.jpg" alt="Full Fridge Bundle artwork">
      <div>
        <h2>The Full Fridge Bundle</h2>
        <p>Every Plugins for Breakfast plugin in one bundle, with new ones added as they come out of the oven.</p>
      </div>
    </div>
  </section>
  <section class="wrap">
    <h2 class="center">System requirements</h2>
    <div class="cards">
      <div class="card"><h3>Operating system</h3><p>macOS on Apple silicon or Intel Macs.</p></div>
      <div class="card"><h3>Formats</h3><p>Audio Unit (AU) and VST3, in 64-bit hosts.</p></div>
      <div class="card"><h3>Hosts</h3><p>Logic Pro, Ableton Live, FL Studio, Cubase, Reaper, Studio One, GarageBand and other AU or VST3 hosts.</p></div>
      <div class="card"><h3>Licence</h3><p>Online activation, valid on up to three computers. Free 3-day trial for every paid plugin.</p></div>
    </div>
  </section>""")

page("about.html", "About", "About Escae Studios, the independent audio software company behind Plugins for Breakfast.", """  <section class="hero page-title wrap">
    <span class="badge">About us</span>
    <h1>About <span>Escae Studios</span></h1>
    <p class="lede">An independent audio software company that builds tools for people who make music.</p>
  </section>
  <section class="wrap narrow">
    <div class="prose">
      <h2>Who we are</h2>
      <p>Escae Studios is a small, independent company that develops and sells audio software. We write our own signal processing, design our own interfaces and support our customers directly.</p>
      <h2>What we make</h2>
      <p>Our first product line, <b>Plugins for Breakfast</b>, is a set of sixteen audio effect plugins for macOS in the Audio Unit and VST3 formats. They cover the everyday jobs of music production: distortion, equalisation, compression, gating, clipping, delay, reverb, chorus, panning, filtering, tape saturation, granular effects and mastering.</p>
      <p>Each plugin is presented as a hand-made felt scene, such as a breakfast table, a bakery or a noodle bar, where every object is a working control. The goal is serious audio quality with an interface that is quick to learn and enjoyable to use.</p>
      <h2>How we work</h2>
      <ul>
        <li>Every paid plugin can be tried free for 3 days before buying.</li>
        <li>One licence covers up to three of your computers.</li>
        <li>Butter Spread, our stereo widener, is free for everyone.</li>
        <li>Plugins are tested in major hosts before release, and updates are free within a version.</li>
      </ul>
      <h2>Get in touch</h2>
      <p>For support, sales, press or partnership questions, email <a href="mailto:hello@escaestudios.com">hello@escaestudios.com</a>. We reply to every message.</p>
    </div>
  </section>""")

page("support.html", "Support", "Help with installing, activating and using Escae Studios plugins.", """  <section class="hero page-title wrap">
    <span class="badge">Support</span>
    <h1>How can we <span>help?</span></h1>
    <p class="lede">Email <a href="mailto:hello@escaestudios.com">hello@escaestudios.com</a> and we'll get back to you, usually within one working day.</p>
  </section>
  <section class="wrap narrow">
    <div class="prose">
      <h2>Frequently asked questions</h2>
      <details><summary>How do I install a plugin?</summary><p>Download the installer for macOS and open it. It places the AU version in /Library/Audio/Plug-Ins/Components and the VST3 version in /Library/Audio/Plug-Ins/VST3. Then restart your music software or rescan plugins.</p></details>
      <details><summary>My DAW doesn't show the plugin</summary><p>Rescan plugins in your host's preferences. In Logic Pro, open the Plug-in Manager and reset or rescan the plugin. Make sure your host supports AU or VST3 on macOS.</p></details>
      <details><summary>How does the free trial work?</summary><p>Every paid plugin runs fully for 3 days so you can try it in your own projects. After that, activate a licence to keep using it.</p></details>
      <details><summary>How many computers can I use?</summary><p>Each licence can be activated on up to three computers. To move a licence, deactivate it on the old machine first, or email us and we'll reset it.</p></details>
      <details><summary>Do you support Windows?</summary><p>Our plugins launch on macOS first. Tell us at hello@escaestudios.com if you'd like a Windows version.</p></details>
      <details><summary>I lost my licence or download link</summary><p>Email us from the address you bought with and we'll send it again.</p></details>
      <h2>Contact</h2>
      <p>Email: <a href="mailto:hello@escaestudios.com">hello@escaestudios.com</a><br>When you write, please include the plugin name, your macOS version, your music software and what happened.</p>
    </div>
  </section>""")

page("privacy.html", "Privacy Policy", "Privacy policy for Escae Studios and Plugins for Breakfast.", """  <section class="hero page-title wrap">
    <h1>Privacy <span>Policy</span></h1>
    <p class="meta">Last updated 7 November 2026</p>
  </section>
  <section class="wrap narrow">
    <div class="prose">
      <h2>Who we are</h2>
      <p>This policy explains how Escae Studios ("we", "us") handles personal information when you visit escaestudios.com, contact us, or buy and use our software.</p>
      <h2>What we collect</h2>
      <ul>
        <li><b>Contact details</b> you send us, such as your name and email address when you write to us or join our mailing list.</li>
        <li><b>Purchase and licence details</b> needed to sell and activate our plugins, such as your email address, order number and the activation status of your licence. Payments are processed by our store and payment providers; we never see or store your full card details.</li>
        <li><b>Activation data</b>: when a plugin activates, it sends a licence key and a device identifier so we can limit each licence to three computers.</li>
      </ul>
      <p>This website does not use advertising or tracking cookies.</p>
      <h2>How we use it</h2>
      <ul>
        <li>To deliver, activate and support the software you bought.</li>
        <li>To answer your messages.</li>
        <li>To send product news, only if you asked to receive it. Every email has an unsubscribe link.</li>
      </ul>
      <h2>Sharing</h2>
      <p>We do not sell your personal information. We share it only with service providers that help us run the business, such as our online store, payment processor and email provider, and only as needed for those services, or when the law requires it.</p>
      <h2>Keeping and deleting data</h2>
      <p>We keep purchase and licence records for as long as you have a licence and as required for tax and accounting. You can ask us to see, correct or delete your personal information at any time.</p>
      <h2>Contact</h2>
      <p>Privacy questions: <a href="mailto:hello@escaestudios.com">hello@escaestudios.com</a></p>
    </div>
  </section>""")

page("terms.html", "Terms of Use", "Terms of use and software licence terms for Escae Studios products.", """  <section class="hero page-title wrap">
    <h1>Terms of <span>Use</span></h1>
    <p class="meta">Last updated 7 November 2026</p>
  </section>
  <section class="wrap narrow">
    <div class="prose">
      <h2>About these terms</h2>
      <p>These terms apply to escaestudios.com and to software made by Escae Studios, including the Plugins for Breakfast range. By using the website or our software you agree to them.</p>
      <h2>Software licence</h2>
      <ul>
        <li>When you buy a plugin, you get a personal, non-exclusive, non-transferable licence to use it on up to three computers that you own or control.</li>
        <li>You may use our plugins to make music and audio for any purpose, including commercial releases. Your recordings are yours.</li>
        <li>You may not resell, share, rent, reverse engineer or redistribute the software or licence keys.</li>
        <li>Trial versions are for evaluation only and stop working when the trial ends unless a licence is activated.</li>
        <li>Free plugins may be used under the same terms at no cost, unless they come with their own open-source licence.</li>
      </ul>
      <h2>Purchases and refunds</h2>
      <p>Because every paid plugin has a free trial, please try it before buying. If something isn't working, contact us and we'll help, or we'll consider a refund where the software doesn't work as described.</p>
      <h2>Updates</h2>
      <p>We may release updates that fix problems or add features. Updates within a major version are free.</p>
      <h2>No warranty</h2>
      <p>The software is provided "as is". We work hard to make it reliable, but we can't promise it will be free of errors or suit every system. To the extent the law allows, we aren't liable for indirect losses, such as lost work or lost profits, arising from its use. Please keep backups of your projects.</p>
      <h2>Website content</h2>
      <p>All text, images and artwork on this website are owned by Escae Studios and may not be copied without permission.</p>
      <h2>Contact</h2>
      <p><a href="mailto:hello@escaestudios.com">hello@escaestudios.com</a></p>
    </div>
  </section>""")

print("pages written")
