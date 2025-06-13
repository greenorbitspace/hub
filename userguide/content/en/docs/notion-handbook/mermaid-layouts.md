---
title: Mermaid Layouts
linkTitle: Mermaid Layouts
date: '2025-05-06T14:19:00Z'
weight: 0
description: Guide for creating advanced Mermaid diagrams, including Gantt charts,
  flowcharts, and sequence diagrams, with examples for layout options and formatting.
---


<!-- Unsupported block type: image -->

## Mermaid diagrams

For the main Mermaid documentation please refer to the Tools and Tips page.

This page is intended to help out with some advanced layout options for Mermaid diagrams such as creating diagrams that are wider than the handbook main content area.

### Gantt

```plain text
gantt
    title A Gantt Diagram
    dateFormat  YYYY-MM-DD
    section Section
    A task           :a1, 2014-01-01, 30d
    Another task     :after a1  , 20d
    section Another
    Task in sec      :2014-01-12  , 12d
    another task      : 24d
```

### Flowchart (centered)

```plain text
graph TD
    A[Christmas] -->|Get money| B(Go shopping)
    B --> C{Let me think}
    C -->|One| D[Laptop]
    C -->|Two| E[iPhone]
    C -->|Three| F[fa:fa-car Car]
```

### Sequence Diagram (right aligned)

```plain text
sequenceDiagram
    Alice->>+John: Hello John, how are you?
    Alice->>+John: John, can you hear me?
    John-->>-Alice: Hi Alice, I can hear you!
    John-->>-Alice: I feel great!
```

### Gantt (wide scrollable)

```plain text
gantt
    title A Gantt Diagram
    dateFormat  YYYY-MM-DD
    section Section
    A task           :a1, 2014-01-01, 30d
    Another task     :after a1  , 20d
    section Another
    Task in sec      :2014-01-12  , 12d
    another task      : 24d
```