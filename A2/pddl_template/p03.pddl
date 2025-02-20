(define (problem p3-dungeon)
  (:domain Dungeon)

  ; Naming convention:
  ; - loc-{i}-{j} refers to the location at the i'th column and j'th row (starting in top left corner)
  ; - c{i}{j}{h}{k} refers to the corridor connecting loc-{i}-{j} and loc-{h}-{k}
  (:objects
    loc-3-4 loc-4-5 loc-1-2 loc-2-2 loc-3-2 loc-3-3 loc-2-5 loc-1-3 loc-2-1 loc-1-4 loc-3-5 loc-2-4 loc-4-4 loc-2-3 loc-4-3 - location
    c2122 c1222 c2232 c1213 c1223 c2223 c3223 c3233 c1323 c2333 c1314 c2314 c2324 c2334 c3334 c1424 c2434 c2425 c2535 c3545 c4544 c4443 - corridor
    key1 key2 key3 key4 key5 key6 - key
  )

  (:init

    ; Hero location and carrying status
    (hero-at loc-2-1)
    (arm-free)

    ; Locationg <> Corridor Connections
    (connected-corridor loc-2-1 c2122)
    (connected-corridor loc-2-2 c2122)

    (connected-corridor loc-1-2 c1222)
    (connected-corridor loc-2-2 c1222)

    (connected-corridor loc-2-2 c2232)
    (connected-corridor loc-3-2 c2232)

    (connected-corridor loc-1-2 c1213)
    (connected-corridor loc-1-3 c1213)

    (connected-corridor loc-1-2 c1223)
    (connected-corridor loc-2-3 c1223)

    (connected-corridor loc-2-2 c2223)
    (connected-corridor loc-2-3 c2223)

    (connected-corridor loc-3-2 c3223)
    (connected-corridor loc-2-3 c3223)

    (connected-corridor loc-3-2 c3233)
    (connected-corridor loc-3-3 c3233)

    (connected-corridor loc-1-3 c1323)
    (connected-corridor loc-2-3 c1323)

    (connected-corridor loc-2-3 c2333)
    (connected-corridor loc-3-3 c2333)

    (connected-corridor loc-1-3 c1314)
    (connected-corridor loc-1-4 c1314)

    (connected-corridor loc-2-3 c2314)
    (connected-corridor loc-1-4 c2314)

    (connected-corridor loc-2-3 c2324)
    (connected-corridor loc-2-4 c2324)

    (connected-corridor loc-2-3 c2334)
    (connected-corridor loc-3-4 c2334)

    (connected-corridor loc-3-3 c3334)
    (connected-corridor loc-3-4 c3334)

    (connected-corridor loc-1-4 c1424)
    (connected-corridor loc-2-4 c1424)

    (connected-corridor loc-2-4 c2434)
    (connected-corridor loc-3-4 c2434)

    (connected-corridor loc-2-4 c2425)
    (connected-corridor loc-2-5 c2425)

    (connected-corridor loc-2-5 c2535)
    (connected-corridor loc-3-5 c2535)

    (connected-corridor loc-3-5 c3545)
    (connected-corridor loc-4-5 c3545)

    (connected-corridor loc-4-5 c4544)
    (connected-corridor loc-4-4 c4544)

    (connected-corridor loc-4-4 c4443)
    (connected-corridor loc-4-3 c4443)


    ; Key locations
    (key-at loc-2-1 key1)
    (key-at loc-2-3 key2)
    (key-at loc-2-3 key3)
    (key-at loc-2-3 key4)
    (key-at loc-2-3 key5)
    (key-at loc-4-4 key6)

    ; Locked corridors
    
    ; red locks
    (is-locked c1223 red)
    (is-locked c2223 red)
    (is-locked c3223 red)
    
    (is-locked c1323 red)
    (is-locked c2333 red)
    
    (is-locked c2314 red)
    (is-locked c2324 red)
    (is-locked c2334 red)

    ;other locks
    (is-locked c2425 purple)
    (is-locked c2535 green)
    (is-locked c3545 purple)
    (is-locked c4544 rainbow)
    
    ; red locks
    (lock c1223)
    (lock c2223)
    (lock c3223)
    
    (lock c1323)
    (lock c2333)
    
    (lock c2314)
    (lock c2324)
    (lock c2334)

    ;other locks
    (lock c2425)
    (lock c2535)
    (lock c3545)
    (lock c4544)

    ; Risky corridors
    (is-risky c1223)
    (is-risky c2223)
    (is-risky c3223)
    (is-risky c1323)
    (is-risky c2333)
    (is-risky c2314)
    (is-risky c2324)
    (is-risky c2334)

    ; Key colours
    (key-colour key1 red)
    (key-colour key2 green)
    (key-colour key3 green)
    (key-colour key4 purple)
    (key-colour key5 purple)
    (key-colour key6 rainbow)

    ; Key usage properties (one use, two use, etc)
    (key-oneuse key2)
    (key-oneuse key3)
    (key-oneuse key4)
    (key-oneuse key5)
    
    (key-useable key1)
    (key-useable key2)
    (key-useable key3)
    (key-useable key4)
    (key-useable key5)
    (key-useable key6)

  )
  (:goal
    (and
      ; Hero's final location goes here
      (hero-at loc-4-3)
    )
  )

)
