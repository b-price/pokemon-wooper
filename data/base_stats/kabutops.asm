	db KABUTOPS ; 141

	db  60, 115, 105,  80,  65,  70
	;   hp  atk  def  spd  sat  sdf

	db ROCK, WATER
	db 45 ; catch rate
	db 201 ; base exp
	db NO_ITEM ; item 1
	db NO_ITEM ; item 2
	db 31 ; gender
	db 100 ; unknown
	db 30 ; step cycles to hatch
	db 5 ; unknown
	dn 6, 6 ; frontpic dimensions
	db 0, 0, 0, 0 ; padding
	db MEDIUM_FAST ; growth rate
	dn AMPHIBIAN, INVERTEBRATE ; egg groups

	; tmhm
	tmhm CURSE, TOXIC, ROLLOUT, SWORDS_DANCE, HIDDEN_POWER, ICY_WIND, ICE_BEAM, BLIZZARD, HYPER_BEAM, PROTECT, RAIN_DANCE, GIGA_DRAIN, RETURN, DIG, MUD_SLAP, DOUBLE_TEAM, SWAGGER, SANDSTORM, STONE_EDGE, REST, ATTRACT, THIEF, BODY_SLAM, ROCK_SLIDE, FURY_CUTTER, SUBSTITUTE, SCALD, X_SCISSOR, ENDURE, CUT, SURF, WHIRLPOOL, WATERFALL, ROCK_SMASH, AQUA_TAIL, DOUBLE_EDGE, EARTH_POWER, HEADBUTT, IRON_HEAD, SEISMIC_TOSS, SLEEP_TALK
	; end
