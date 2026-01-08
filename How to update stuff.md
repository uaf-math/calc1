- To update header on website, go to _data/general.yml
- To update body of landing page, go to index.md
- To update menu _data/toc.yaml
  - To share schedule, you need to "Publish" the sheet and copy the resulting URL into the menu.
- To update things like the recitations schedule, you must not only create the appropriate content file (e.g., _data/recitations_s2026.yml), you must update the file name reference in recitaitons.md
- Can't use ":" in an argument in a .yml file. Example:

  - _data/recitations-s2026.yml

    - | `95` | `95` | `      blank: M251f21_Recitation_Integration-Extra.pdf`    |
      | ---- | ---- | ---------------------------------------------------------- |
      | `96` | `96` | `      filled: M251f21_Recitation_Integration-Extra-s.pdf` |
      | `97` |      | `-      video:    - Week: Week 14`                         |
      |      | `97` | `+      video:`                                            |

      The problem is apparently the : in the title on line 97.