```mermaid

%%{
  init: {
    'theme': 'base',
    'themeVariables': {
      'fontFamily': 'Noto Sans, Arial, Sans-Serif',
      'primaryColor': '#31b4aa',
      'primaryTextColor': '#071625',
      'primaryBorderColor': '#2564a1',
      'lineColor': '#d5dddc',
      'secondaryColor': '#3a8dcb',
      'tertiaryColor': '#fff',
      'sectionBkgColor': '#52bdd7',
      'altSectionBkgColor': '#d5dddc'
    }
  }
}%%

gantt
    dateFormat  YYYY-MM-DD
    title       IDiS Roadmap
    tickInterval 3month
    axisFormat %b %y

    section Publications
    Whitepaper Copyright and licensing SMART : milestone, 2026-03-31, 1d
    Whitepaper AI Testing       : milestone, 2025-11-31, 1d
    Whitepaper Authoring SPEC         : milestone, 2025-08-30, 1d
    ReqIF SPEC             : milestone, done, 2025-02-15, 1d
    Whitepaper 3           : milestone, done, 2024-04-01, 1d
    Whitepaper 2           : milestone, done, 2022-05-01, 1d
    Whitepaper 1           : milestone, done, 2021-06-01, 1d

    section Authoring
    Authoring Guideline    : active, 2023-11-29, 2025-08-01

    section Requirements
    Math. Formulas         : done, 2021-07-01, 2022-06-01
    ReqIF                  : active, 2023-08-31, 2026-08-31
    ReqSyntax              : active, 2024-05-01, 2025-08-30
    Kimba (ReqIF Usage) :  2025-12-01, 2027-12-01

    section Delivery
    Asset Admin. Shell A   : done, 2021-09-01, 2022-09-01
    Asset Admin. Shell B   : done, 2023-09-15, 2024-06-26
    Dataspaces             : 2025-10-01, 2027-10-01

    section Usage
    Copyright Copyright and licensing of SMART Standards : 2025-09-01, 2027-10-01
    SMART Standards for SMEs : 2025-08-01, 2026-08-01

    section AI/Automation
    Auto. Conformity Assess: done, 2021-07-01, 2022-10-01
    Standards LLM          : done, 2022-04-01, 2023-01-01
    Scalable AI Assessment : active, 2024-08-01, 2025-12-31 
```

| Element                   | Timeframe              | Description                                                              | Link                                                                                   |
|---------------------------|------------------------|--------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| **Authoring SPEC**        | until Apr 2025         | Specification for structured, machine-readable authoring of standards    | [dke.de/idis](https://www.dke.de/idis)                                                 |
| **ReqIF SPEC**            | completed Feb 2025     | Definition of requirements exchange format (ReqIF)                       | [Github](https://github.com/DIN-DKE/DIN_DKE_SPEC_99200__ReqIF_interpretation_for_public_standards) |
| **Whitepaper 3**          | completed Apr 2024     | Economic impact and value of SMART Standards                             | [Download](https://www.dke.de/resource/blob/3089126/88a04b253f37d8d7e2e42364e1d4a8c4/idis-whitepaper-3-de---download-data.pdf)     |
| **Whitepaper 2**          | completed May 2022     | 11 practical use cases for SMART Standards                               | [Download](https://www.dke.de/resource/blob/2738944/ee15f94ad21d3e351cf190b2a87a9e7b/idis-whitepaper-2-de---download-data.pdf)     |
| **Whitepaper 1**          | completed Jun 2021     | Digitalization scenarios and maturity levels for standards               | [Download](https://www.dke.de/resource/blob/2034796/0a674443fb9a40f87ae5387e5b2fd2ba/idis-whitepaper-1-de---download-data.pdf)     |
| **Authoring Guideline**   | 2023–2025              | Guidance for content creation in digital standardization workflows       |                   |
| **ReqSyntax**             | 2024–2025              | Syntax rules for machine-readable normative requirements                 |                    |
| **Asset Admin. Shell B**  | 2023–2024              | Integration of standard content as AASX (Asset Administration Shell)     | [IDiS Pilots](https://www.dke.de/idis/pilotprojekte/normintegration-in-die-verwaltungsschale)                                       |
| **Scalable AI Assessment**| 2024–2025              | AI-based automated conformity checking for SMART Standards               | [AI Conformity Check](https://bit.ly/kipruefung-smart-standards)  |
