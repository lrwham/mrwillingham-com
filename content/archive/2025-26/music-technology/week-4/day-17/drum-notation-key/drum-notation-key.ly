\version "2.24.0"

\header {
  title = "Drum Notation KEY"
  tagline = ""
}

\paper {
  indent = 0
  ragged-right = ##f
}

% Place the two cowbells at distinct vertical positions: the Mambo
% cowbell in the space above the staff, and the Cha-cha cowbell on
% the first ledger line above, so it has a visible ledger line.
mydrumstyle = #(alist->hash-table
  (append '((cowbell default #f 5)
            (hcb default #f 6))
          (hash-table->alist drums-style)))

drumPitchNames =
  #(append '((hcb . hcb)) drumPitchNames)

drumsMusic = \drummode {
  \stemUp
  bd4^\markup \bold "DRUMS"
  sn ss
  \parenthesize sn
  \tweak NoteHead.style #'cross sn
  tomh toml tomfl
}

drumLyrics = \lyricmode {
  \markup \center-column { Bass Drum }
  \markup \center-column { Snare Drum }
  \markup \center-column { Snare Cross Stick }
  \markup \center-column { Snare Ghost Note }
  \markup \center-column { Snare Rimshot }
  \markup { "Tom1" }
  \markup { "Tom2" }
  \markup \center-column { Floor Tom }
}

cymbalsMusic = \drummode {
  \override Staff.LedgerLineSpanner.length-fraction = #1.2
  \stemUp
  hh4^\markup \bold "CYMBALS"
  hho hhp cymr
  \tweak NoteHead.style #'do \tweak NoteHead.font-size #2 rb
  cymc^\markup \bold "COWBELLS"
  \tweak NoteHead.style #'harmonic-black \tweak NoteHead.font-size #2 cb
  \tweak NoteHead.style #'harmonic-black \tweak NoteHead.font-size #2 hcb
}

cymbalLyrics = \lyricmode {
  \markup \center-column { "Hi-Hat" }
  \markup \center-column { "Hi-Hat" Open }
  \markup \center-column { "Hi-Hat" "w/Foot" }
  \markup \center-column { Ride Cymbal }
  \markup \center-column { Ride Bell }
  \markup \center-column { Crash Cymbal }
  \markup \center-column { Mambo Cowbell }
  \markup \center-column { "Cha-cha" Cowbell }
}

\score {
  <<
    \new DrumStaff \with {
      \remove "Bar_engraver"
      \remove "Time_signature_engraver"
    } \new DrumVoice = "drumsV" { \drumsMusic }
    \new Lyrics \lyricsto "drumsV" \drumLyrics
  >>
  \layout { }
  \midi { }
}

\score {
  <<
    \new DrumStaff \with {
      \remove "Bar_engraver"
      \remove "Time_signature_engraver"
      drumStyleTable = #mydrumstyle
    } \new DrumVoice = "cymbalsV" { \cymbalsMusic }
    \new Lyrics \lyricsto "cymbalsV" \cymbalLyrics
  >>
  \layout { }
  \midi { }
}
