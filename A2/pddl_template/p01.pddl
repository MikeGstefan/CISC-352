(define (problem p1-dungeon)
  (:domain Dungeon)

  ; Naming convention:
  ; - loc-{i}-{j} refers to the location at the i'th column and j'th row (starting in top left corner)
  ; - c{i}{j}{h}{k} refers to the corridor connecting loc-{i}-{j} and loc-{h}-{k}
  (:objects
    loc-3-1 loc-1-2 loc-2-2 loc-3-2 loc-4-2 loc-2-3 loc-3-3 loc-2-4 loc-3-4 loc-4-4 - location
    key1 key2 key3 key4 - key
    c3132 c1222 c2232 c3242 c2223 c3233 c2333 c2324 c3334 c2434 c3444 - corridor
  )

  (:init

    ; Hero location and carrying status
    (hero-at loc-1-2)
    (arm-free)

    ; Locationg <> Corridor Connections
    (connected-corridor loc-3-1 c3132)
    (connected-corridor loc-3-2 c3132)

    (connected-corridor loc-1-2 c1222)
    (connected-corridor loc-2-2 c1222)

    (connected-corridor loc-2-2 c2232)
    (connected-corridor loc-3-2 c2232)

    (connected-corridor loc-3-2 c3242)
    (connected-corridor loc-4-2 c3242)

    (connected-corridor loc-2-2 c2223)
    (connected-corridor loc-2-3 c2223)

    (connected-corridor loc-3-2 c3233)
    (connected-corridor loc-3-3 c3233)

    (connected-corridor loc-2-3 c2333)
    (connected-corridor loc-3-3 c2333)

    (connected-corridor loc-2-3 c2324)
    (connected-corridor loc-2-4 c2324)

    (connected-corridor loc-3-3 c3334)
    (connected-corridor loc-3-4 c3334)

    (connected-corridor loc-2-4 c2434)
    (connected-corridor loc-3-4 c2434)

    (connected-corridor loc-3-4 c3444)
    (connected-corridor loc-4-4 c3444)

    ; Key locations
    (key-at loc-2-2 key1)
    (key-at loc-2-4 key2)
    (key-at loc-4-2 key3)
    (key-at loc-4-4 key4)

    ; Locked corridors
    (is-locked c3132 rainbow)
    (is-locked c3242 purple)
    (is-locked c2324 red)
    (is-locked c2434 red)
    (is-locked c3444 yellow)
    
    (lock c3132)
    (lock c3242)
    (lock c2324)
    (lock c2434)
    (lock c3444)

    ; Risky corridors
    (is-risky c2324)
    (is-risky c2434)

    ; Key colours
    (key-colour key1 red)
    (key-colour key2 yellow)
    (key-colour key3 rainbow)
    (key-colour key4 purple)

    ; Key usage properties (one use, two use, etc)
    (key-useable key1)
    (key-useable key2)
    (key-useable key3)
    (key-useable key4)
    
    (key-twouse key2)
    (key-oneuse key3)
    (key-oneuse key4)
  )
  (:goal
    (and
      (hero-at loc-3-1)
    )
  )

)
