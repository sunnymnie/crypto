\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{messari}[2022/09/01 Notes]

%% Load base
\LoadClass[a4paper]{article}

% Load additional packages and commands.
% \RequirePackage{custom}

\RequirePackage{geometry}
\RequirePackage{fontspec}
\RequirePackage{tocloft}
\RequirePackage{setspace}
\RequirePackage{graphicx}

\setmainfont{Avenir Next}

%% Additional TeX/LaTeX code...


\renewcommand{\cfttoctitlefont}{\normalfont\Large}% Remove \bfseries from ToC title
\renewcommand{\cftsecfont}{}% Remove \bfseries from section titles in ToC
\renewcommand{\cftsecpagefont}{}% Remove \bfseries from section titles' page in ToC

% \newcommand{\Example}{
% \par
% \textsl{Example }
% }




\endinput

