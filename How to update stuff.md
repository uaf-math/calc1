- To update header on website, go to _data/general.yml

- To update body of landing page, go to index.md

- To update menu _data/toc.yaml
  - To share schedule, you need to "Publish" the sheet from Google Sheets File menu and copy the resulting URL into the menu.
  
    
  
- To update things like the recitations schedule, you must not only create the appropriate content file (e.g., _data/recitations_s2026.yml), you must update the file name reference in recitaitons.md

- Can't use ":" in an argument in a .yml file. Example:

  - _data/recitations-s2026.yml

    - | `95` | `95` | `      blank: M251f21_Recitation_Integration-Extra.pdf`    |
      | ---- | ---- | ---------------------------------------------------------- |
      | `96` | `96` | `      filled: M251f21_Recitation_Integration-Extra-s.pdf` |
      | `97` |      | `-      video:    - Week: Week 14`                         |
      |      | `97` | `+      video:`                                            |

      The problem is apparently the : in the title on line 97.
  
- To get quizzes to show current stuff (process similar for Exams):

  - Edit quizzes.md in root folder to reflect current semester.
  - Make sure you've archived a copy as the version for the previous semester. You'll want to add an entry to the top of the list that points to the old semester of quizzes. Fortunately the format and file locations and naming conventions are pretty self explanatory.
  - You'll need a folder in assets/quizzes for the current semester.
  - As semester progresses, add entries to quizzes-SEMESTER.yml in _data folder. Formatting of entries can be seen in prior .yml files.
  - This is in fact, the general scheme for most items that show up in the toc.yaml
  - I think.
