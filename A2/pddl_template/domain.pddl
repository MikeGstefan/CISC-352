(define (domain Dungeon)

    (:requirements
        :typing
        :negative-preconditions
        :conditional-effects
        :equality
    )

    ; Do not modify the types
    (:types
        location colour key corridor
    )

    ; Do not modify the constants
    (:constants
        red yellow green purple rainbow - colour
    )

    ; You may introduce whatever predicates you would like to use
    (:predicates

        ; One predicate given for free!
        (hero-at ?loc - location)
        
        ; If room adjacent to corridor
        (connected-corridor ?loc - location ?cor - corridor) 
        
        ; Room Proporties
        (is-messy ?loc - location)
        (key-at ?room - location ?item - key)

        ; Corridor Proporties 
        (is-collapsed ?cor - corridor)
        (is-risky ?cor - corridor)
        (is-locked ?cor - corridor ?col - colour)
        (lock ?cor)

        (key-colour ?item - key ?col - colour)
        
        ; Key Useability Tracker
        (key-useable ?item - key)
        (key-oneuse ?item - key)
        (key-twouse ?item - key)
        
        ;If Hero's arm is free and what they have
        (arm-free)
        (has-key ?item - key)


    )

    ; IMPORTANT: You should not change/add/remove the action names or parameters

    ;Hero can move if the
    ;    - hero is at current location ?from,
    ;    - hero will move to location ?to,
    ;    - corridor ?cor exists between the ?from and ?to locations
    ;    - there isn't a locked door in corridor ?cor
    ;Effects move the hero, and collapse the corridor if it's "risky" (also causing a mess in the ?to location)
    (:action move

        :parameters (?from ?to - location ?cor - corridor)

        :precondition (and

            (hero-at ?from) (connected-corridor ?from ?cor) (connected-corridor ?to ?cor) 
                (not(lock ?cor)) (not (is-collapsed ?cor)) (not(= ?from ?to))

        )

        :effect (and 
            
            (not (hero-at ?from)) (hero-at ?to)
                (when (is-risky ?cor) 
                (and (is-collapsed ?cor) (is-messy ?to)) )


        )
    )

    ;Hero can pick up a key if the
    ;    - hero is at current location ?loc,
    ;    - there is a key ?k at location ?loc,
    ;    - the hero's arm is free,
    ;    - the location is not messy
    ;Effect will have the hero holding the key and their arm no longer being free
    (:action pick-up

        :parameters (?loc - location ?k - key)

        :precondition (and

            
            (hero-at ?loc) (key-at ?loc ?k) 
                (arm-free) (not(is-messy ?loc))
                

        )

        :effect (and
                
            
            (not(arm-free)) (not (key-at ?loc ?k)) (has-key ?k)

        )
    )

    ;Hero can drop a key if the
    ;    - hero is holding a key ?k,
    ;    - the hero is at location ?loc
    ;Effect will be that the hero is no longer holding the key
    (:action drop

        :parameters (?loc - location ?k - key)

        :precondition (and

            (hero-at ?loc) (not(arm-free)) (has-key ?k)
        )

        :effect (and

            (key-at ?loc ?k) (arm-free) (not(has-key ?k))
        )
    )


    ;Hero can use a key for a corridor if
    ;    - the hero is holding a key ?k,
    ;    - the key still has some uses left,
    ;    - the corridor ?cor is locked with colour ?col,
    ;    - the key ?k is if the right colour ?col,
    ;    - the hero is at location ?loc
    ;    - the corridor is connected to the location ?loc
    ;Effect will be that the corridor is unlocked and the key usage will be updated if necessary
    (:action unlock

        :parameters (?loc - location ?cor - corridor ?col - colour ?k - key)

        :precondition (and

            (not(arm-free)) (has-key ?k) (key-useable ?k) (connected-corridor ?loc ?cor)
                (key-colour ?k ?col) (hero-at ?loc) (is-locked ?cor ?col) (lock ?cor)

        )

        :effect (and

            
            (not (is-locked ?cor ?col))
            (not (lock ?cor))

            (when (key-oneuse ?k) 
                (and (not (key-useable ?k)) (not (key-oneuse ?k))) )
            

            (when (key-twouse ?k)
                (and (not (key-twouse ?k)) (key-oneuse ?k)) )

        )
    )

    ;Hero can clean a location if
    ;    - the hero is at location ?loc,
    ;    - the location is messy
    ;Effect will be that the location is no longer messy
    (:action clean

        :parameters (?loc - location)

        :precondition (and

            (is-messy ?loc) (hero-at ?loc)

        )

        :effect (and

            (not (is-messy ?loc))

        )
    )

)
