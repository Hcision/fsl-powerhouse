#!/usr/bin/env python3
"""Rebuild assets/banner.svg. Run after adding or removing an agent or a skill."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FAMILIES = [
    ("FIELD SERVICE", "#38bdf8", [
        "Architecture", "Workforce", "Scheduling", "Dispatch console", "Maintenance", "Mobile", "Execution",
        "Inventory", "Assets", "Customer", "Access", "Integration", "Analytics", "Agentforce", "Troubleshooting"]),
    ("PLATFORM", "#4ade80", ["Apex", "LWC", "Flow", "Security", "Architecture"]),
    ("DELIVERY", "#fbbf24", ["Quality audit", "Ticket delivery", "Release watch"]),
    ("KNOWLEDGE", "#c4b5fd", ["Live docs", "Knowledge grounding"]),
]
PANEL_X, PANEL_W, PAD, CHIP_H, GAP = 716, 520, 18, 26, 6


def panel():
    parts, y = [], 20
    for label, color, chips in FAMILIES:
        parts.append(f'<circle cx="24" cy="{y + 5}" r="5" fill="{color}"/>')
        parts.append(f'<text x="36" y="{y + 10}" font-size="12" font-weight="700" letter-spacing="1.4" fill="{color}">{label}</text>')
        x, y = PAD, y + 20
        for chip in chips:
            width = round(len(chip) * 6.9 + 20)
            if x + width > PANEL_W - PAD:
                x, y = PAD, y + CHIP_H + GAP
            parts.append(f'<rect x="{x}" y="{y}" width="{width}" height="{CHIP_H}" rx="13" fill="{color}"/>')
            parts.append(f'<text x="{x + width / 2:g}" y="{y + 18}" font-size="13" font-weight="600" text-anchor="middle" fill="#071a33">{chip}</text>')
            x += width + GAP
        y += CHIP_H + 16
    return "\n      ".join(parts), y + 2


def main():
    agents = len(list((ROOT / "agents").glob("*.md")))
    skills = len(list((ROOT / "skills").glob("*/SKILL.md")))
    assert skills == sum(len(chips) for _, _, chips in FAMILIES), "Update FAMILIES to match skills/"
    body, panel_h = panel()
    height = max(360, panel_h + 60)
    top = (height - panel_h) // 2
    mid = height // 2
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 {height}" width="1280" height="{height}" role="img" aria-label="FSL Powerhouse: source-grounded Salesforce and Field Service delivery for Claude Code. {skills} skills in four families: Field Service, Platform, Delivery and Knowledge.">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#071a33"/>
      <stop offset="0.55" stop-color="#0b3a6b"/>
      <stop offset="1" stop-color="#0a5a8f"/>
    </linearGradient>
    <linearGradient id="title" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#ffffff"/>
      <stop offset="1" stop-color="#7dd3fc"/>
    </linearGradient>
    <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M40 0H0V40" fill="none" stroke="#ffffff" stroke-opacity="0.05"/>
    </pattern>
    <clipPath id="round"><rect width="1280" height="{height}" rx="24"/></clipPath>
  </defs>
  <g clip-path="url(#round)" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif">
    <rect width="1280" height="{height}" fill="url(#bg)"/>
    <rect width="1280" height="{height}" fill="url(#grid)"/>
    <circle cx="1130" cy="20" r="220" fill="#38bdf8" fill-opacity="0.10"/>
    <circle cx="60" cy="{height + 20}" r="180" fill="#f59e0b" fill-opacity="0.08"/>
    <g transform="translate({PANEL_X} {top})">
      <rect width="{PANEL_W}" height="{panel_h}" rx="16" fill="#071a33" fill-opacity="0.45" stroke="#ffffff" stroke-opacity="0.16"/>
      {body}
    </g>
    <g transform="translate(72 {mid - 118})">
      <rect width="64" height="64" rx="16" fill="#38bdf8"/>
      <path d="M36 10 18 36h12l-4 18 20-28H33z" fill="#071a33"/>
    </g>
    <text x="72" y="{mid + 10}" font-size="66" font-weight="800" fill="url(#title)" letter-spacing="-1.5">FSL Powerhouse</text>
    <text x="74" y="{mid + 50}" font-size="22" fill="#dbeafe">Source-grounded Salesforce and Field Service</text>
    <text x="74" y="{mid + 79}" font-size="22" fill="#dbeafe">delivery for Claude Code</text>
    <g font-size="15" font-weight="600" fill="#e0f2fe">
      <rect x="72" y="{mid + 106}" width="104" height="30" rx="15" fill="#ffffff" fill-opacity="0.12"/>
      <text x="124" y="{mid + 126}" text-anchor="middle">{agents} agents</text>
      <rect x="186" y="{mid + 106}" width="96" height="30" rx="15" fill="#ffffff" fill-opacity="0.12"/>
      <text x="234" y="{mid + 126}" text-anchor="middle">{skills} skills</text>
      <rect x="292" y="{mid + 106}" width="170" height="30" rx="15" fill="#ffffff" fill-opacity="0.12"/>
      <text x="377" y="{mid + 126}" text-anchor="middle">live official docs</text>
    </g>
  </g>
</svg>
'''
    (ROOT / "assets" / "banner.svg").write_text(svg, encoding="utf-8")
    print(f"banner.svg: {agents} agents, {skills} skills, {height}px high")


if __name__ == "__main__":
    main()
