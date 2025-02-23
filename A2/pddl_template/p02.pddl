(define (problem p2-dungeon)
  (:domain Dungeon)

  ; Naming convention:
  ; - loc-{i}-{j} refers to the location at the i'th column and j'th row (starting in top left corner)
  ; - c{i}{j}{h}{k} refers to the corridor connecting loc-{i}-{j} and loc-{h}-{k}
  (:objects
    loc-2-1 loc-1-2 loc-2-2 loc-3-2 loc-4-2 loc-2-3 - location
    key1 key2 key3 key4 - key
    c2122 c1222 c2232 c3242 c2223 - corridor
  )

  (:init

    ; Hero location and carrying status
    (hero-at loc-2-2)
    (arm-free)
    
    ; Locationg <> Corridor Connections
    (connected-corridor loc-2-1 c2122)
    (connected-corridor loc-2-2 c2122)

    (connected-corridor loc-1-2 c1222)
    (connected-corridor loc-2-2 c1222)

    (connected-corridor loc-2-2 c2232)
    (connected-corridor loc-3-2 c2232)

    ; (connected-corridor loc-3-2 c3242)

    (connected-corridor loc-2-2 c2223)
    (connected-corridor loc-2-3 c2223)
    
    (connected-corridor loc-4-2 c3242)
    (connected-corridor loc-3-2 c3242)

    ; Key locations
    (key-at loc-2-1 key1)
    (key-at loc-1-2 key2)
    (key-at loc-2-2 key3)
    (key-at loc-2-3 key4)

    ; Locked corridors
    (is-locked c2122 purple)
    (is-locked c1222 yellow)
    (is-locked c2223 green)
    (is-locked c2232 yellow)
    (is-locked c3242 rainbow)
    
    (lock c2122 )
    (lock c1222 )
    (lock c2223 )
    (lock c2232 )
    (lock c3242 )


    ; Risky corridors

    ; No RED LOCKS = NO RISKY CORRIDORS

    ; Key colours
    (key-colour key1 green)
    (key-colour key2 rainbow)
    (key-colour key3 purple)
    (key-colour key4 yellow)

    ; Key usage properties (one use, two use, etc)
    (key-oneuse key1)
    (key-oneuse key3)

    (key-twouse key4)
    
    (key-useable key1)
    (key-useable key2)
    (key-useable key3)
    (key-useable key4)

  )
  (:goal
    (and
      ; Hero's final location goes here
      (hero-at loc-4-2)
    )
  )

)
