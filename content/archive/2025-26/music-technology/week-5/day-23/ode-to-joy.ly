\version "2.26.0"

\header {
  title = "Ode to Joy"
  composer = "Ludwig van Beethoven"
  tagline = ##f
}

\layout {
  \context {
    \Score
    autoBeaming = ##f
  }
}

PartPOneVoiceOne = \relative b' {
  \clef "treble" \time 4/4 \key g \major b4 b4 c4
  d4 | % 1
  d4 c4 b4 a4 | % 2
  g4 g4 a4 b4 | % 3
  b4. a8 a2 | % 4
  b4 b4 c4 d4 | % 5
  d4 c4 b4 a4 | \break % 6
  g4 g4 a4 b4 | % 7
  a4. g8 g2 \bar "||" % 8
  a4 a4 b4 g4 | % 9
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
  \clef "bass" \time 4/4 \key g \major <g b d>1 | % 1
  <fis a d>1 | % 2
  <g b d>1 | % 3
  <g b d>2 <fis a d>2 | % 4
  <g b d>1 | % 5
  <fis a d>1 | % 6
  <g b d>1 | % 7
  <fis a d>2 <g b d>2 \bar "||" % 8
  d,2 <d' g b>2 | % 9
  d,2 <d' g b>2 | % 10
  d,2 <d' g b>2 | % 11
  cis2 <d fis a>2 \bar "||" % 12
  <g b d>1 | % 13
  <fis a d>1 | % 14
  <g b d>1 | % 15
  <fis a d>2 <g ~ b ~ d ~>2 | % 16
  <g b d>1 \bar "|."
}

\score {
  <<
    \new PianoStaff <<
      \set PianoStaff.instrumentName = "Piano"
      \set PianoStaff.shortInstrumentName = "Pno."
      \new Staff <<
        \mergeDifferentlyDottedOn
        \mergeDifferentlyHeadedOn
        \context Voice = "PartPOneVoiceOne" {
          \PartPOneVoiceOne
        }
      >>
      \new Staff <<
        \mergeDifferentlyDottedOn
        \mergeDifferentlyHeadedOn
        \context Voice = "PartPOneVoiceFive" {
          \PartPOneVoiceFive
        }
      >>
    >>
  >>
}
