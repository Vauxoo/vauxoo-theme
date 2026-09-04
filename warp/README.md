# Vauxoo themes for Warp

The Vauxoo brand palettes as [Warp](https://www.warp.dev) terminal themes,
matching the [Vauxoo Theme for VSCode](https://marketplace.visualstudio.com/items?itemName=vauxoo.vauxoo-theme)
so editor and terminal share one identity.

## What's inside

| File | Flavor |
|---|---|
| `vauxoo-dark.yaml` | Vauxoo Dark — colors only |
| `vauxoo-light.yaml` | Vauxoo Light — colors only |
| `vauxoo-vakyro.yaml` | Vauxoo Vakyro (mascot purples/pink) — colors only |
| `vauxoo-dark-vakyro.yaml` | Vauxoo Dark **+ Vakyro watermark** background |
| `vauxoo-light-vakyro.yaml` | Vauxoo Light **+ Vakyro watermark** background |
| `vauxoo-vakyro-vakyro.yaml` | Vauxoo Vakyro **+ Vakyro watermark** background |
| `vauxoo-*-bg.png` | The watermark backgrounds (Vakyro, the Vauxoo mascot, bottom-right at ~10% opacity) |

Each theme defines accent, background, foreground and the 16 ANSI terminal
colors with the activity semantics used across Vauxoo tooling: green = OK /
running, gold = warning / needs you, red = error / stopped.

## Install

The `.png` files must land in the same folder as the `.yaml` files — the
watermark themes reference them by relative path.

**macOS**

```sh
git clone https://github.com/Vauxoo/vauxoo-theme
mkdir -p ~/.warp/themes && cp vauxoo-theme/warp/*.yaml vauxoo-theme/warp/*.png ~/.warp/themes/
```

**Linux**

```sh
git clone https://github.com/Vauxoo/vauxoo-theme
mkdir -p ~/.local/share/warp-terminal/themes
cp vauxoo-theme/warp/*.yaml vauxoo-theme/warp/*.png ~/.local/share/warp-terminal/themes/
```

**Windows (PowerShell)**

```powershell
git clone https://github.com/Vauxoo/vauxoo-theme
New-Item -ItemType Directory -Force "$env:APPDATA\warp\Warp\data\themes" | Out-Null
Copy-Item vauxoo-theme\warp\*.yaml, vauxoo-theme\warp\*.png "$env:APPDATA\warp\Warp\data\themes\"
```

## Activate

Warp → **Settings → Appearance → Theme** (macOS shortcut: `Ctrl+Cmd+T`) and
pick any **Vauxoo** variant. Restart the tab if the background image doesn't
show right away.

## Also in the official gallery

The colors-only trio is submitted to Warp's official themes repository:
[warpdotdev/themes#170](https://github.com/warpdotdev/themes/pull/170).
