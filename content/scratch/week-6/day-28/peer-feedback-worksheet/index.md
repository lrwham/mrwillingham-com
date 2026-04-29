---
type: bare
toc: false
title: Peer Feedback Worksheet
draft: false
---

<style>
  /* Letter portrait: 8.5in x 11in. With 0.4in top/bottom margins the
     printable area is 10.2in tall, so each of the three panels on a
     sheet is exactly 3.4in tall. */
  @page {
    size: letter portrait;
    margin: 0.4in 0.5in;
  }
  * { box-sizing: border-box; }
  body {
    font-family: Arial, Helvetica, sans-serif;
    margin: 0;
    padding: 0;
    color: #000;
  }
  .sheet {
    width: 100%;
    height: 10.2in;          /* exact printable height on letter */
    display: flex;
    flex-direction: column;
  }
  .panel {
    height: 3.4in;           /* exactly 1/3 of the printable sheet */
    flex: 0 0 3.4in;
    padding: 0.15in 0.15in 0.1in 0.15in;
    overflow: hidden;
    page-break-inside: avoid;
    break-inside: avoid;
  }
  .cut {
    border: none;
    border-top: 1.5px dashed #aaa;
    margin: 0;
    height: 0;
    position: relative;
  }
  .cut::before {
    content: "\2702";
    position: absolute;
    left: -18px;
    top: -10px;
    font-size: 13px;
    color: #aaa;
    line-height: 1;
  }
  .page-break { page-break-before: always; }
  @media print {
    html, body { width: 7.5in; }
    .sheet { height: 10.2in; }
  }
  .panel-title {
    font-size: 13px;
    font-weight: bold;
    margin: 0 0 3px 0;
    text-align: center;
    letter-spacing: 0.01em;
  }
  .panel-subtitle {
    font-size: 9px;
    text-align: center;
    color: #555;
    margin: 0 0 5px 0;
  }
  .panel h2 {
    font-size: 11px;
    font-weight: bold;
    margin: 6px 0 3px 0;
    border-bottom: 1.5px solid #000;
    padding-bottom: 1px;
    text-transform: uppercase;
    letter-spacing: 0.04em;
  }
  .panel h3 {
    font-size: 10px;
    font-weight: bold;
    margin: 5px 0 2px 0;
  }
  .section-label {
    font-size: 9px;
    font-weight: bold;
    text-transform: uppercase;
    letter-spacing: 0.04em;
    color: #666;
    margin: 0 0 2px 0;
  }
  .name-row {
    display: flex;
    gap: 16px;
    margin-bottom: 4px;
    font-size: 10px;
  }
  .name-row span {
    flex: 1;
    border-bottom: 1px solid #000;
    padding-bottom: 1px;
  }
  .reminder {
    border: 1px solid #bbb;
    background: #f7f7f7;
    padding: 4px 7px;
    font-size: 9px;
    line-height: 1.45;
    margin-bottom: 5px;
  }
  .lines { margin: 2px 0 5px 0; }
  .lines .ln {
    border-bottom: 1px solid #bbb;
    height: 20px;
    margin-bottom: 1px;
  }
  .check-row {
    display: flex;
    gap: 20px;
    font-size: 10px;
    margin: 3px 0 5px 0;
    flex-wrap: wrap;
  }
  .check-row label { display: flex; align-items: center; gap: 4px; }
  .checklist { margin: 4px 0 0 0; }
  .checklist .cr {
    display: flex;
    align-items: flex-start;
    gap: 6px;
    font-size: 10px;
    margin-bottom: 4px;
    line-height: 1.3;
  }
</style>

<div class="sheet">
  <div class="panel">
    <div class="panel-title">Peer Feedback Worksheet</div>
    <div class="panel-subtitle">Day 28 &mdash; Video Game Design Project</div>
    <div class="name-row">
      <span><strong>Your Name:</strong></span>
      <span><strong>Your Group:</strong></span>
      <span><strong>Period:</strong></span>
    </div>
    <div class="name-row">
      <span><strong>Group You Are Reviewing:</strong></span>
      <span><strong>Game Title:</strong></span>
    </div>
    <div class="reminder">
      <strong>Reminder:</strong> Play the game like someone who has never seen it before. Don't ask the other team for help &mdash; figure it out on your own and note what confuses you. Feedback should be <strong>honest and kind</strong>. Don't say "it's bad" &mdash; say what specifically isn't working and what could fix it. Don't just say "it's good" &mdash; name something that can be improved.
    </div>
    <h2>Part 1: Presentation Feedback</h2>
    <h3>1. What part of the presentation was clear and engaging?</h3>
    <div class="lines"><div class="ln"></div><div class="ln"></div></div>
    <h3>2. What part could be clearer or more interesting?</h3>
    <div class="lines"><div class="ln"></div><div class="ln"></div></div>
    <h3>3. How long did the presentation feel?</h3>
    <div class="check-row">
      <label><input type="checkbox"> Too short</label>
      <label><input type="checkbox"> About right (3&ndash;5 min)</label>
      <label><input type="checkbox"> Too long</label>
    </div>
  </div>
  <hr class="cut">
  <div class="panel">
    <div class="panel-title">Peer Feedback Worksheet</div>
    <div class="panel-subtitle">Day 28 &mdash; Video Game Design Project</div>
    <div class="name-row">
      <span><strong>Your Name:</strong></span>
      <span><strong>Your Group:</strong></span>
      <span><strong>Period:</strong></span>
    </div>
    <div class="name-row">
      <span><strong>Group You Are Reviewing:</strong></span>
      <span><strong>Game Title:</strong></span>
    </div>
    <div class="reminder">
      <strong>Reminder:</strong> Play the game like someone who has never seen it before. Don't ask the other team for help &mdash; figure it out on your own and note what confuses you. Feedback should be <strong>honest and kind</strong>. Don't say "it's bad" &mdash; say what specifically isn't working and what could fix it. Don't just say "it's good" &mdash; name something that can be improved.
    </div>
    <h2>Part 1: Presentation Feedback</h2>
    <h3>1. What part of the presentation was clear and engaging?</h3>
    <div class="lines"><div class="ln"></div><div class="ln"></div></div>
    <h3>2. What part could be clearer or more interesting?</h3>
    <div class="lines"><div class="ln"></div><div class="ln"></div></div>
    <h3>3. How long did the presentation feel?</h3>
    <div class="check-row">
      <label><input type="checkbox"> Too short</label>
      <label><input type="checkbox"> About right (3&ndash;5 min)</label>
      <label><input type="checkbox"> Too long</label>
    </div>
  </div>
  <hr class="cut">
  <div class="panel">
    <div class="panel-title">Peer Feedback Worksheet</div>
    <div class="panel-subtitle">Day 28 &mdash; Video Game Design Project</div>
    <div class="name-row">
      <span><strong>Your Name:</strong></span>
      <span><strong>Your Group:</strong></span>
      <span><strong>Period:</strong></span>
    </div>
    <div class="name-row">
      <span><strong>Group You Are Reviewing:</strong></span>
      <span><strong>Game Title:</strong></span>
    </div>
    <div class="reminder">
      <strong>Reminder:</strong> Play the game like someone who has never seen it before. Don't ask the other team for help &mdash; figure it out on your own and note what confuses you. Feedback should be <strong>honest and kind</strong>. Don't say "it's bad" &mdash; say what specifically isn't working and what could fix it. Don't just say "it's good" &mdash; name something that can be improved.
    </div>
    <h2>Part 1: Presentation Feedback</h2>
    <h3>1. What part of the presentation was clear and engaging?</h3>
    <div class="lines"><div class="ln"></div><div class="ln"></div></div>
    <h3>2. What part could be clearer or more interesting?</h3>
    <div class="lines"><div class="ln"></div><div class="ln"></div></div>
    <h3>3. How long did the presentation feel?</h3>
    <div class="check-row">
      <label><input type="checkbox"> Too short</label>
      <label><input type="checkbox"> About right (3&ndash;5 min)</label>
      <label><input type="checkbox"> Too long</label>
    </div>
  </div>
</div>

<div class="sheet page-break">
  <div class="panel">
    <h2>Part 2: Prototype Feedback</h2>
    <h3>4. What works well?</h3>
    <div class="section-label">Name one specific thing that functions correctly and feels good to play.</div>
    <div class="lines"><div class="ln"></div><div class="ln"></div></div>
    <h3>5. What's confusing or broken?</h3>
    <div class="section-label">Describe anything that didn't make sense, got stuck, crashed, or was impossible to figure out without help.</div>
    <div class="lines"><div class="ln"></div><div class="ln"></div><div class="ln"></div></div>
    <h3>6. One suggestion</h3>
    <div class="section-label">Give one concrete, actionable idea to improve the game. Be specific.</div>
    <div class="lines"><div class="ln"></div><div class="ln"></div></div>
    <h2>Checklist &mdash; before you hand this to the other group</h2>
    <div class="checklist">
      <div class="cr"><input type="checkbox"> I named something specific that works well.</div>
      <div class="cr"><input type="checkbox"> I described something confusing or broken.</div>
      <div class="cr"><input type="checkbox"> I gave one concrete suggestion to improve the game.</div>
      <div class="cr"><input type="checkbox"> I gave feedback on both the presentation and the prototype.</div>
      <div class="cr"><input type="checkbox"> My feedback is honest, specific, and kind.</div>
    </div>
  </div>
  <hr class="cut">
  <div class="panel">
    <h2>Part 2: Prototype Feedback</h2>
    <h3>4. What works well?</h3>
    <div class="section-label">Name one specific thing that functions correctly and feels good to play.</div>
    <div class="lines"><div class="ln"></div><div class="ln"></div></div>
    <h3>5. What's confusing or broken?</h3>
    <div class="section-label">Describe anything that didn't make sense, got stuck, crashed, or was impossible to figure out without help.</div>
    <div class="lines"><div class="ln"></div><div class="ln"></div><div class="ln"></div></div>
    <h3>6. One suggestion</h3>
    <div class="section-label">Give one concrete, actionable idea to improve the game. Be specific.</div>
    <div class="lines"><div class="ln"></div><div class="ln"></div></div>
    <h2>Checklist &mdash; before you hand this to the other group</h2>
    <div class="checklist">
      <div class="cr"><input type="checkbox"> I named something specific that works well.</div>
      <div class="cr"><input type="checkbox"> I described something confusing or broken.</div>
      <div class="cr"><input type="checkbox"> I gave one concrete suggestion to improve the game.</div>
      <div class="cr"><input type="checkbox"> I gave feedback on both the presentation and the prototype.</div>
      <div class="cr"><input type="checkbox"> My feedback is honest, specific, and kind.</div>
    </div>
  </div>
  <hr class="cut">
  <div class="panel">
    <h2>Part 2: Prototype Feedback</h2>
    <h3>4. What works well?</h3>
    <div class="section-label">Name one specific thing that functions correctly and feels good to play.</div>
    <div class="lines"><div class="ln"></div><div class="ln"></div></div>
    <h3>5. What's confusing or broken?</h3>
    <div class="section-label">Describe anything that didn't make sense, got stuck, crashed, or was impossible to figure out without help.</div>
    <div class="lines"><div class="ln"></div><div class="ln"></div><div class="ln"></div></div>
    <h3>6. One suggestion</h3>
    <div class="section-label">Give one concrete, actionable idea to improve the game. Be specific.</div>
    <div class="lines"><div class="ln"></div><div class="ln"></div></div>
    <h2>Checklist &mdash; before you hand this to the other group</h2>
    <div class="checklist">
      <div class="cr"><input type="checkbox"> I named something specific that works well.</div>
      <div class="cr"><input type="checkbox"> I described something confusing or broken.</div>
      <div class="cr"><input type="checkbox"> I gave one concrete suggestion to improve the game.</div>
      <div class="cr"><input type="checkbox"> I gave feedback on both the presentation and the prototype.</div>
      <div class="cr"><input type="checkbox"> My feedback is honest, specific, and kind.</div>
    </div>
  </div>
</div>
