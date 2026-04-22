\version "2.26.0"
% automatically converted by musicxml2ly from Ode to Joy.mxl
\pointAndClickOff

%% additional definitions required by the score:
D = \tweak Stem.direction #DOWN \etc
U = \tweak Stem.direction #UP \etc


\header {
  title = \markup \normal-text \normalsize \fontsize #6.032 "Ode to Joy"
  composer = \markup \normal-text \normalsize "Ludwig van Beethoven"
  "work-title" = "Untitled score"
  "id: composer" = "Composer / arranger"
  "id: software" = "MuseScore 4.5.1"
  "id: encoding-date" = "2026-04-22"
}
#(set-global-staff-size 19.91442529133858)
\paper {
  paper-width = 21.59\cm
  paper-height = 27.94\cm
  top-margin = 1.5\cm
  bottom-margin = 1.5\cm
  left-margin = 1.5\cm
  right-margin = 1.5\cm
  indent = 1.66\cm
  short-indent = 1.33\cm
}
\layout {
  \context {
    \Staff
    printKeyCancellation = ##f
  }
  \context {
    \Score
    autoBeaming = ##f
  }
}
PartPOneVoiceOne = \relative b' {
  \clef "treble" \numericTimeSignature \time 4/4 \key g \major \D b4 \D b4 \D c4
  \D d4 | % 1
  \D d4 \D c4 \D b4 \U a4 | % 2
  \U g4 \U g4 \U a4 \D b4 | % 3
  \D b4. \U a8 \U a2 | % 4
  \D b4 \D b4 \D c4 \D d4 | % 5
  \D d4 \D c4 \D b4 \U a4 | % 6
  \U g4 \U g4 \U a4 \D b4 | % 7
  \U a4. \U g8 \U g2 \bar "||" % 8
  \U a4 \U a4 \D b4 \U g4 | % 9

  \barNumberCheck #10
  \U a4 \D b8 [ \D c8 ] \D b4 \U g4 | % 10
  \U a4 \D b8 [ \D c8 ] \D b4 \U a4 | % 11
  \U g4 \U a4 \U d,2 \bar "||" % 12
  \D b'4 \D b4 \D c4 \D d4 | % 13
  \D d4 \D c4 \D b4 \U a4 | % 14
  \U g4 \U g4 \U a4 \D b4 | % 15
  \U a4. \U g8 \U g2 ~ | % 16
  g1 \bar "|."
}

PartPOneVoiceFive = \relative g {
  \clef "bass" \numericTimeSignature \time 4/4 \key g \major <g b d>1 | % 1
  <fis a d>1 | % 2
  <g b d>1 | % 3
  \D <g b d>2 \D <fis a d>2 | % 4
  <g b d>1 | % 5
  <fis a d>1 | % 6
  <g b d>1 | % 7
  \D <fis a d>2 \D <g b d>2 \bar "||" % 8
  \U d,2 \D <d' g b>2 | % 9

  \barNumberCheck #10
  \U d,2 \D <d' g b>2 | % 10
  \U d,2 \D <d' g b>2 | % 11
  \U cis2 \D <d fis a>2 \bar "||" % 12
  <g b d>1 | % 13
  <fis a d>1 | % 14
  <g b d>1 | % 15
  \D <fis a d>2 \D <g ~ b ~ d ~>2 | % 16
  <g b d>1 \bar "|."
}


% The score definition
\score {
  <<
    \new PianoStaff <<
      \set PianoStaff.instrumentName = "Piano"
      \set PianoStaff.shortInstrumentName = "Pno."
      \context Staff = "1" <<
        \mergeDifferentlyDottedOn
        \mergeDifferentlyHeadedOn
        \context Voice = "PartPOneVoiceOne" {
          \PartPOneVoiceOne
        }
      >>
      \context Staff = "2" <<
        \override Staff.BarLine.allow-span-bar = ##f
        \mergeDifferentlyDottedOn
        \mergeDifferentlyHeadedOn
        \context Voice = "PartPOneVoiceFive" {
          \PartPOneVoiceFive
        }
      >>
    >>
  >>
  \layout {}
  % To create MIDI output, uncomment the following line:
  % \midi { \tempo 4 = 100 }
}

