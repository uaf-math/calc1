\NeedsTeXFormat{LaTeX2e} 
\ProvidesClass{homework}[2007/02/19]
\newif\ifusingminion \usingminionfalse
\DeclareOption{minion}{\usingminiontrue}
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{article}}
\ProcessOptions\relax

\LoadClass[12pt]{article} 

\RequirePackage{amssymb,amsmath,amsthm}
\RequirePackage[top=1in, bottom=1in, left=1.25in, right=1.25in]{geometry}
\RequirePackage{fancyhdr}

\ifusingminion
\RequirePackage[lf]{MinionPro}
%% Error message wierdness from the MinionPro package.  The following line fixes it. I don't know why.
\let\mathdollar\undefined 
\else
\usepackage{times}
\fi

%% We define two new enviroments for listing problems. I originally used the LaTeX list mechanism
%% for this, but it doesn't get along with the wrapfigure package for nice figures. So we hand
%% code it instead.
%%
%% The usual flow is:
%%
%% \begin{problems}
%% \hproblem stuff
%% \hproblem stuff
%%   \begin{subproblems}
%%     \subprob stuff
%%     \subprob stuff
%%   \end{subproblems}
%% \end{problems}
%%
%% The problem and aproblem environments are closely related.  The aproblem enviroment has formatting
%% more appropriate for a list of assigned problems, whereas the problem enviroment works better 
%% for problems with solutions.  Maybe I should just make this an option at the beginning of the
%% enviroment.

\newcounter{probcount}
\newcounter{subprobcount}
\newlength\probsep
\newlength\pshrinking
\newif\iffirstprob

\newenvironment{problems}%
{\ifhmode\unskip\par\fi\setcounter{probcount}{0}\probsep\parskip\addtolength{\probsep}{8pt minus 8pt}%
\firstprobtrue}%
{\ifhmode\unskip \par\fi}%

\newenvironment{aproblems}%
  {\ifhmode\unskip\par\fi\setcounter{probcount}{0}\probsep\parskip
  \sbox\@tempboxa{\textbf{9.}}\pshrinking\wd\@tempboxa\advance\pshrinking\labelsep
  \let\hproblem\aproblem
  \advance\linewidth -\pshrinking
  \advance\@totalleftmargin\pshrinking
  \advance\leftskip\pshrinking}%
  {\ifhmode\unskip \par\fi\advance\leftskip-\pshrinking}%

\newenvironment{subproblems}%
  {\begin{enumerate}\listlabel{\alph{\thelistlabel})}%
  %% Make the enumerate environment think we are making a list in a list:
  \global \@newlistfalse}%
  {\end{enumerate}}%

\newcommand{\hproblem}{%
  \setcounter{subprobcount}{0}%
  \stepcounter{probcount}%
  \def\@currentlabel{\arabic{probcount}}%
  \ifhmode
    \unskip \par
  \fi
  \addpenalty{-4000}%
  \iffirstprob\else\addvspace\probsep\fi
  \firstprobfalse
  \hskip -\labelwidth\hskip -\labelsep 
  \hbox to\labelwidth{\hss\textbf{\arabic{probcount}.}}\hskip\labelsep
}%

\newcommand{\aproblem}{%
  \setcounter{subprobcount}{0}%
  \stepcounter{probcount}%
  \def\@currentlabel{\arabic{probcount}}%
  \ifhmode
    \unskip \par
  \fi
%  \addpenalty{-4000}%
  \iffirstprob\else\addvspace\probsep\fi
  \firstprobfalse
  \hskip -\labelwidth\hskip -\labelsep 
  \hbox to\labelwidth{\hss\textbf{\arabic{probcount}.}}\hskip\labelsep
}%


\newcommand{\subprob}{\item\def\@currentlabel{\arabic{probcount}\alph{\thelistlabel}}}
\newcommand{\skipproblem}{\stepcounter{probcount}}

%% The localhead command puts a label on top of a paragraph -- handy for labels
%% like "Solution:"
\newskip\restoreparskip
\newcommand{\localhead}[1]{\par\smallskip\textbf{#1}%
%% The following arcane code was added to make the localhead enviroment get along
%% with the ams theorem enviroment (which is based on the latex list enviroment).
%% previously, the command was {\par\smallskip\textbf{#1}\\}, but the list
%% enviroment would also add a par at the end of this paragraph, which would result
%% in an extra blank line.  Our solution now is to put in our own par, but with
%% none of the parskip glue that adds extra space between paragraphs.
  \restoreparskip\parskip\parskip 0pt\par\nobreak\noindent\parskip\restoreparskip}%
\newcommand\solution{\localhead{Solution:}}
\newcommand\subsol{\stepcounter{subprobcount}\localhead{Solution, part \alph{subprobcount}:}}

% Some handy little commands for laying out solutions.
\newcommand\define[1]{\textit{#1}}
\newcommand\Hint{\textit{Hint:}\ }
\newcommand\pref[1]{Problem \textbf{\ref{#1}}}

%% The following commands put defined left and right headers on the top, and a page number
%% on the bottom of all pages beyond page 1
\pagestyle{fancy}
\fancyfoot[C]{\ifnum \value{page} > 1\relax\thepage\fi}
\fancyhead[L]{\ifx\@doclabel\@empty\else\@doclabel\fi}
\fancyhead[R]{\ifx\@docdate\@empty\else\@docdate\fi}
\headheight 15pt
\def\doclabel#1{\gdef\@doclabel{#1}}
\def\docdate#1{\gdef\@docdate{#1}}

%% General formatting parameters
\parindent 0pt
\parskip 6pt plus 1pt


%% The begin/end mechanism is a little cumbersome when doing theorems and proofs:
%% \begin{theorem} ... \end{theorem} \begin{proof} ... \end{proof}
%%
%% Instead, we do:
%% \theorem .... \Proof ... \EOP
%% or
%%
%% \theorem .... \NoProof
%%
%% To use this mechanism, use:
%%
%% \eztheorem{startcommand}[counter]{label}
%%
%% E.g. \eztheorem{theorem}{Theorem} makes a \theorem command
%%      \eztheorem{lemma}[theorem]{Lemma} makes a \lemma command that uses the same
%%  numbering counter as the theorem command. i.e,
%%  Theorem 1, Lemma 2, Theorem 3   vs.   Theorem 1, Lemma 2, Theorem 2
%
\def\eztheorem#1{\ezthmnol@{#1}}
\def\eztheorem#1{\@ifnextchar[{\ezthm@{#1}}{\ezthmnol@{#1}}}
\def\ezthm@#1[#2]#3{\newtheorem{ezthm#1}[ezthm#2]{#3}\expandafter\gdef\csname#1\endcsname{\ezstartthm{ezthm#1}}}

\def\ezthmnol@#1#2{\newtheorem{ezthm#1}{#2}\expandafter\gdef\csname #1\endcsname{\ezstartthm{ezthm#1}}}
\newcommand{\NoProof}{\end{\ezthmenv}\egroup}
\newcommand{\Proof}{\end{\ezthmenv}\egroup\begin{proof}}
\newcommand{\EOP}{\end{proof}}
\def\ezstartthm#1{\bgroup\def\ezthmenv{#1}\begin{\ezthmenv}}
%%
%% Declare the theorem types for problem sets.  
%%
\eztheorem{theorem}{Theorem}
\eztheorem{corollary}[theorem]{Corollary}
\eztheorem{proposition}[theorem]{Proposition}
\eztheorem{lemma}[theorem]{Lemma}


%% The default 'article' class has captions that label figures Figure 1, etc.  This is too 
%% formal for homework sets, so we change \caption so that it just puts the caption text.
%% Here I have just modified the \@makecaption command from the article class.
%% Maybe I should change this in the future to let authors decide whether or not to label a figure.

\long\def\@makecaption#1#2{%
  \vskip\abovecaptionskip
  \sbox\@tempboxa{#2}%
  \ifdim \wd\@tempboxa >\hsize
    #2\par
  \else
    \global \@minipagefalse
    \hb@xt@\hsize{\hfil\box\@tempboxa\hfil}%
  \fi
  \vskip\belowcaptionskip}

%% The default implementation of the proof environment starts a new paragraph at the start of the proof,
%% with the full parskip spacing. This only looks good following a theorem statement 
%% if \parskip is set to zero.  We've got a medium sized parskip, so we overide this 
%% questionable decision.
\renewenvironment{proof}[1][\proofname]{\par
  \pushQED{\qed}%
  \normalfont \topsep6\p@\@plus6\p@\relax
  \trivlist
  \@topsep \topsep
  \item[\hskip\labelsep
        \itshape
    #1\@addpunct{.}]\ignorespaces
}{%
  \popQED\endtrivlist\@endpefalse
}

