(define (problem p4-dungeon)
  (:domain Dungeon)

  ; Naming convention:
  ; - loc-{i}-{j} refers to the location at the i'th column and j'th row (starting in top left corner)
  ; - c{i}{j}{h}{k} refers to the corridor connecting loc-{i}-{j} and loc-{h}-{k}
  (:objects
    loc-1-1 loc-1-2 loc-1-3 loc-1-4 loc-2-2 loc-2-3 loc-2-4 loc-3-4 loc-4-4 - location
    key1 key2 key3 key4 key5 key6 - key
    c1112 c1213 c1314 c1222 c1323 c1424 c2434 c3444 - corridor
  )

  (:init

    ; Hero location and carrying status
    (hero-at loc-1-1)
    (arm-free)

    ; Locationg <> Corridor Connections
    (connected-corridor loc-1-1 c1112)
    (connected-corridor loc-1-2 c1112)

    (connected-corridor loc-1-2 c1213)
    (connected-corridor loc-1-3 c1213)

    (connected-corridor loc-1-3 c1314)
    (connected-corridor loc-1-4 c1314)

    (connected-corridor loc-1-2 c1222)
    (connected-corridor loc-2-2 c1222)

    (connected-corridor loc-1-3 c1323)
    (connected-corridor loc-2-3 c1323)

    (connected-corridor loc-1-4 c1424)
    (connected-corridor loc-2-4 c1424)

    (connected-corridor loc-2-4 c2434)
    (connected-corridor loc-3-4 c2434)

    (connected-corridor loc-3-4 c3444)
    (connected-corridor loc-4-4 c3444)


    ; Key locations
    (key-at loc-1-1 key1)
    (key-at loc-1-2 key2)
    (key-at loc-2-3 key3)
    (key-at loc-1-4 key4)
    (key-at loc-4-4 key5)
    (key-at loc-1-3 key6)

    ; Locked corridors
    (is-locked c1222 rainbow)
    (is-locked c2434 purple)
    (is-locked c1112 red)
    (is-locked c1323 yellow)
    (is-locked c1424 yellow)
    (is-locked c1314 green)
    (is-locked c3444 green)
    
    (lock c1222)
    (lock c2434)
    (lock c1112)
    (lock c1323)
    (lock c1424)
    (lock c1314)
    (lock c3444)

    ; Risky corridors
    (is-risky c1112)

    ; Key colours
    (key-colour key1 red)
    (key-colour key2 green)
    (key-colour key3 purple)
    (key-colour key4 yellow)
    (key-colour key5 rainbow)
    (key-colour key6 green)

    ; Key usage properties (one use, two use, etc)
    (key-useable key1)
    (key-useable key2)
    (key-useable key3)
    (key-useable key4)
    (key-useable key5)
    (key-useable key6)
    
    (key-twouse key4)
    (key-oneuse key2)
    (key-oneuse key3)
    (key-oneuse key5)
    (key-oneuse key6)
  )
  (:goal
    (and
      (hero-at loc-2-2)
    )
  )

)
