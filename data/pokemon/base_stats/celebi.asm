	db 100, 100, 100, 100, 100, 100 ; 600 BST
	;   hp  atk  def  spd  sat  sdf

if DEF(FAITHFUL)
	db PSYCHIC, GRASS ; type
else
	db GRASS, FAIRY ; type
endc
	db 45 ; catch rate
	db 64 ; base exp
	db ALWAYS_ITEM_2 ; item 1
	db LUM_BERRY ; item 2
	dn GENDER_UNKNOWN, 15 ; gender ratio, step cycles to hatch
	INCBIN "gfx/pokemon/celebi/front.dimensions" ;dn 5 , 5  frontpic dimensions
if DEF(FAITHFUL)
	abilities_for CELEBI, NATURAL_CURE, NATURAL_CURE, NATURAL_CURE
else
	abilities_for CELEBI, NATURAL_CURE, NATURAL_CURE, MAGIC_GUARD
endc
	db GROWTH_MEDIUM_SLOW ; growth rate
	dn EGG_NONE, EGG_NONE ; egg groups

	ev_yield   3,   0,   0,   0,   0,   0
	;         hp  atk  def  spd  sat  sdf

	; tm/hm learnset
	tmhm CURSE, CALM_MIND, TOXIC, HIDDEN_POWER, SUNNY_DAY, HYPER_BEAM, LIGHT_SCREEN, PROTECT, RAIN_DANCE, GIGA_DRAIN, SAFEGUARD, SOLAR_BEAM, RETURN, PSYCHIC, SHADOW_BALL, DOUBLE_TEAM, REFLECT, SANDSTORM, SWIFT, AERIAL_ACE, SUBSTITUTE, FACADE, REST, DAZZLINGLEAM, ENERGY_BALL, WATER_PULSE, GIGA_IMPACT, U_TURN, FLASH, THUNDER_WAVE, SWORDS_DANCE, CUT, DEFENSE_CURL, DOUBLE_EDGE, DREAM_EATER, EARTH_POWER, ENDURE, SEED_BOMB, SKILL_SWAP, SLEEP_TALK, SUCKER_PUNCH, SWAGGER, TRICK, ZEN_HEADBUTT
	; end
