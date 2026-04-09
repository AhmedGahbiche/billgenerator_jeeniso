# Design System Specification: The Architectural Dark Mode

## 1. Overview & Creative North Star
**The Creative North Star: "The Digital Executive"**

This design system moves beyond the "generic SaaS dashboard" to create an environment that feels like a high-end physical workspace—quiet, authoritative, and frictionless. The "Digital Executive" aesthetic relies on **Tonal Precision** rather than structural decoration. We are building a tool for business automation where trust is earned through clarity and "high-tech" is signaled through depth, not clutter.

To break the "template" look, we utilize **Intentional Asymmetry**. Primary data (like invoice totals) should be anchored with massive, high-contrast typography, while secondary navigation and utility tools are tucked into subtle, low-contrast containers. By overlapping surface layers and utilizing extreme white space, we create a sense of "Air"—a luxury rarely found in dense business tools.

---

### 2. Colors: Tonal Architecture
We do not use color to decorate; we use it to direct attention and define space.

#### The "No-Line" Rule
**Explicit Instruction:** Prohibit the use of 1px solid borders for sectioning. Structural boundaries must be defined solely through background color shifts or subtle tonal transitions.
*   **Implementation:** If a Sidebar sits next to a Main Content area, the Sidebar uses `surface_container_low` (#1C1B1B) while the Main Content uses `surface` (#131313). No vertical line is permitted between them.

#### Surface Hierarchy & Nesting
Treat the UI as a series of physical layers—stacked sheets of obsidian and smoked glass.
*   **Base:** `surface` (#131313)
*   **Secondary Sections:** `surface_container_low` (#1C1B1B)
*   **Interactive Cards:** `surface_container_high` (#2A2A2A)
*   **Elevated Overlays/Modals:** `surface_container_highest` (#353534)

#### The "Glass & Gradient" Rule
For "Pro" high-tech polish, use **Glassmorphism** for floating elements (Top Navs, Context Menus). Use `surface_bright` (#393939) at 60% opacity with a `20px` backdrop-blur. 

#### Signature Textures
Main CTAs (like "Send Invoice") should not be flat. Apply a subtle linear gradient from `primary` (#ADC6FF) to `primary_container` (#4D8EFF) at a 135-degree angle. This provides a "machined" feel that implies power and action.

---

### 3. Typography: The Editorial Voice
We use **Inter** for its mathematical precision. The hierarchy is designed to feel like a high-end financial report.

*   **Display (Large Data Points):** `display-lg` (3.5rem) should be used for the "Hero Number" (e.g., Total Revenue). Keep tracking tight (-0.02em).
*   **Headlines (Section Clarity):** `headline-sm` (1.5rem) uses `on_surface` (#E5E2E1). This is the "Anchor" for each automation module.
*   **Body (Operational):** `body-md` (0.875rem) is our workhorse. Ensure it uses `on_surface_variant` (#C2C6D6) for secondary text to reduce visual noise.
*   **Labels (The "Pro" Look):** All `label-md` and `label-sm` elements should be in **ALL CAPS** with a +0.05em letter spacing to evoke a technical, "instrument cluster" feel.

---

### 4. Elevation & Depth: Tonal Layering
Traditional dropshadows are forbidden. We define depth through light physics and layering.

*   **The Layering Principle:** Place a `surface_container_lowest` (#0E0E0E) card inside a `surface_container_low` (#1C1B1B) section to create a "recessed" well. This is ideal for data entry fields.
*   **Ambient Shadows:** For floating Modals, use a shadow with a `40px` blur, `0%` spread, and `8%` opacity using the `on_background` color. This mimics natural ambient occlusion.
*   **The "Ghost Border" Fallback:** If accessibility requires a stroke (e.g., a focused input), use `outline_variant` (#424754) at **20% opacity**. It should be felt, not seen.
*   **Interactivity:** On hover, a card should not move "up"; instead, transition its background color from `surface_container_high` to `surface_container_highest`.

---

### 5. Components: Precision Tooling

#### High-Tech Data Tables
*   **Rule:** Forbid the use of divider lines between rows.
*   **Separation:** Use a `8px` vertical gap between rows. Each row is its own `surface_container_low` capsule with a `md` (0.375rem) corner radius.
*   **Alignment:** Numbers (Invoices, Amounts) must be Tabular-Lined (Monospaced) for instant scannability.

#### Dynamic Form Fields
*   **State:** The "Neutral" state is a solid `surface_container_highest` fill.
*   **Focus:** Transition the background to `surface_bright` and apply the `primary` (#ADC6FF) "Ghost Border" at 20%.
*   **Success:** Use `secondary` (#4EDEA3) only for the checkmark icon, never the entire box.

#### Elegant "Print/Export" CTAs
*   **Styling:** These are "Secondary" actions. Use the `surface_variant` (#353534) background with `on_surface` text.
*   **Iconography:** Use ultra-thin (1.5pt) line icons to maintain the "Pro" technical aesthetic.

#### Automation Chips
*   **Status:** Active automations use a `secondary_container` (#00A572) background with `on_secondary` (#003824) text.
*   **Shape:** Use the `full` (9999px) roundedness scale to distinguish "objects" from "containers."

---

### 6. Do's and Don'ts

#### Do
*   **Do** use extreme padding (48px+) between major functional blocks to create a "premium" feel.
*   **Do** use `tertiary` (#FFB786) for "Warning" or "Pending" states to distinguish from the "Success" Emerald.
*   **Do** ensure all interactive elements have a minimum 44px hit zone, even if the visual element is smaller.

#### Don't
*   **Don't** use pure black (#000000). It kills the "depth" of the dark mode. Use `surface_container_lowest` (#0E0E0E).
*   **Don't** use standard blue for links. Use `primary_fixed_dim` (#ADC6FF) for a softer, more integrated look.
*   **Don't** use "Center Alignment" for business data. Keep everything on a strict left-aligned editorial grid to reinforce efficiency and speed.