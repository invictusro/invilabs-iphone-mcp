# What you need

The MCP server controls phones that are connected to an Invi Labs account. A phone connects in one of three ways.

## Stock iPhone: Invi Dongle

For an iPhone 11 to 18 that is not jailbroken.

- The [Invi Dongle](https://invidongle.com) plugs into the phone and sends touch and keyboard input.
- The Invi Helper app on the phone streams its screen.
- The phone connects to Invi Labs over Wi-Fi by itself. No Mac, Xcode or WebDriverAgent, and no computer next to the phone.
- The phone stays a normal iPhone, so every App Store app works.
- MCP tools: `devices`, `phone_*` and `wait`.

Two limits that matter to agents: dongle swipes carry no flick speed (use long swipes to change Home Screen pages), and a still App Switcher sends no video frames, so screenshots fail until you leave it.

## Jailbroken iPhone: Invi Link

For an iPhone 7, 8 or X that is already jailbroken. Invi Link does not jailbreak a phone.

- Invi Link is a package installed on the phone. It handles screen video, input and app control on the phone itself.
- Extra MCP tools (`jb_*`): native UI element dumps, tap by text, app lists, open and close apps by bundle ID, lock and unlock, and app containers.
- Containers keep several logins for the same app apart, each with its own device identity and proxy.
- Supported apps: Instagram, Facebook, Threads, X and Reddit. TikTok isn't supported on Invi Link.

## Hosted phone

If you don't have a spare iPhone, rent one hosted by Invi Labs. It shows up in the panel and in `devices` like your own phones. Cloud phones also have proxy and VPN tools (`phone_set_proxy`, `phone_use_vpn`, `phone_set_vpn_location`).

## Account and keys

- Sign up and manage phones at [panel.invilabs.io](https://panel.invilabs.io).
- Signing in from an MCP client creates an API key for that client. To use a key directly, create one under Resources → AI agents (MCP) with the Control permission (`device.control`); add Edit proxy (`device.edit_proxy`) for the network tools.
- Pricing: [invilabs.io/#pricing](https://invilabs.io/#pricing).
