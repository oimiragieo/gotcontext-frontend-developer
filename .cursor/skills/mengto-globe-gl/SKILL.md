---
name: mengto-globe-gl
description: Adapter pointer to canonical skills/mengto-globe-gl for Cursor
---

# mengto-globe-gl (Cursor adapter)

Canonical skill: [`../../../skills/mengto-globe-gl/SKILL.md`](../../../skills/mengto-globe-gl/SKILL.md)

Load and follow the canonical SKILL.md (and sibling refs/scripts there).

## Excerpt

```markdown
---
name: mengto-globe-gl
description: Use when implementing globe.gl (Globe.GL) for 3D globe data visualization with WebGL/ThreeJS, including setup, data layers (points, arcs, polygons, labels), and integration patterns in plain HTML or React.
---

# Globe.GL Skill

## Workflow
1. Confirm environment (plain HTML, framework, React bindings) and the data layers needed.
2. Provide a minimal quick-start snippet plus the layer-specific fields.
3. Add interactions or extra layers only if requested.
4. Call out container sizing and performance considerations.

## Quick start (ESM)
```html
<script type="module">
  import Globe from 'globe.gl';

  const myGlobe = new Globe(document.getElementById('globe'))
    .globeImageUrl(myImageUrl)
    .pointsData(myData);
</script>
```

## Quick start (script tag)
```html
<script src="//cdn.jsdelivr.net/npm/globe.gl"></script>
<script>
  const myGlobe = new Globe(document.getElementById('globe'))
    .globeImageUrl(myImageUrl)
```
