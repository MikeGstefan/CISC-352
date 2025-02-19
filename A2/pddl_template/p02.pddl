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
    (hero-at loc-1-1)
    (arm-free)
    
    ; Locationg <> Corridor Connections
    (connected-corridor 2-1 2122)
    (connected-corridor 2-2 2122)

    (connected-corridor 1-2 1222)
    (connected-corridor 1-2 1222)

    (connected-corridor 2-2 2232)
    (connected-corridor 3-2 2232)

    (connected-corridor 3-2 3242)
    (connected-corridor 3-4 3242)

    (connected-corridor 2-2 2223)
    (connected-corridor 2-3 2223)

    ; Key locations
    (key-at 2-1 key1)
    (key-at 1-2 key2)
    (key-at 2-2 key3)
    (key-at 2-3 key4)

    ; Locked corridors
    (is-locked 2122 purple)
    (is-locked 1222 yellow)
    (is-locked 2223 green)
    (is-locked 2232 yellow)
    (is-locked 3242 rainbow)


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
