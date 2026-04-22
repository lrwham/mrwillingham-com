\version "2.26.0"
\pointAndClickOff

\header {
  title = \markup \normal-text \normalsize \fontsize #6.032 "Ode to Joy"
  composer = \markup \normal-text \normalsize "Ludwig van Beethoven"
  tagline = ##f
}
#(set-global-staff-size 19.91442529133858)
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
  \clef "treble" \numericTimeSignature \time 4/4 \key g \major b4 b4 c4
  d4 | % 1
  d4 c4 b4 a4 | % 2
  g4 g4 a4 b4 | % 3
  b4. a8 a2 | % 4
  b4 b4 c4 d4 | % 5
  d4 c4 b4 a4 | \break % 6
  g4 g4 a4 b4 | % 7
  a4. g8 g2 \bar "||" % 8
  a4 a4 b4 g4 | % 9

  \barNumberCheck #10
  a4 b8 [ c8 ] b4 g4 | % 10
  a4 b8 [ c8 ] b4 a4 | % 11
  g4 a4 d,2 \bar "||" \break % 12
  b'4 b4 c4 d4 | % 13
  d4 c4 b4 a4 | % 14
  g4 g4 a4 b4 | % 15
  a4. g8 g2 ~ | % 16
  g1 \bar "|."
}

PartPOneVoiceFive = \relative g {
  \clef "bass" \numericTimeSignature \time 4/4 \key g \major <g b d>1 | % 1
  <fis a d>1 | % 2
  <g b d>1 | % 3
  <g b d>2 <fis a d>2 | % 4
  <g b d>1 | % 5
  <fis a d>1 | % 6
  <g b d>1 | % 7
  <fis a d>2 <g b d>2 \bar "||" % 8
  d,2 <d' g b>2 | % 9

  \barNumberCheck #10
  d,2 <d' g b>2 | % 10
  d,2 <d' g b>2 | % 11
  cis2 <d fis a>2 \bar "||" % 12
  <g b d>1 | % 13
  <fis a d>1 | % 14
  <g b d>1 | % 15
  <fis a d>2 <g ~ b ~ d ~>2 | % 16
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
