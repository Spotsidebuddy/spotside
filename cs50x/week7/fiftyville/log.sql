-- Keep a log of any SQL queries you execute as you solve the mystery.

--check accident reports
SELECT * FROM crime_scene_reports WHERE year = 2024 AND month = 7 AND day = 28;

--see witness accounts
sqlite> SELECT * FROM interviews WHERE year = 2024 AND day = 28 AND month = 7

--check bakery camera
SELECT * FROM bakery_security_logs WHERE year = 2024 AND day = 28 AND month = 7 AND hour = 10 and minute > 15;
-- 5P2BI95| 94KL13X| 6P58WS2| 4328GD8| G412CB7| L93JTIZ| 322W7JE| 0NTHK55| 1106N58

--check atm transactions on Leggett Street
select * FROM atm_transactions Where year = 2024 AND day = 28 AND month = 7 and atm_location = 'Leggett Street';
--narrow transactions from atm
select account_number
FROM atm_transactions
WHERE year = 2024
AND day = 28
AND month = 7
AND atm_location = 'Leggett Street'
AND transaction_type = 'withdraw';
-- ids: 28500762, 28296815 76054385 49610011 16153065 25506511 81061156 26013199
--see who the belong to
SELECT person_id
FROM bank_accounts
WHERE account_number in (
    select account_number
    FROM atm_transactions
    WHERE year = 2024
    AND day = 28
    AND month = 7
    AND atm_location = 'Leggett Street'
    AND transaction_type = 'withdraw')
-- LIST OF PEOPLE by person_id|
-- 686048| 514354| 458378| 395717| 396669| 467400| 449774| 438727

-- Who are these people?
SELECT * FROM people WHERE id in (686048, 514354, 458378, 395717, 396669, 467400, 449774, 438727) AND license_plate in
(SELECT license_plate FROM bakery_security_logs WHERE year = 2024 AND day = 28 AND month = 7 AND hour = 10 and minute > 15);

--check phonecalls with duration less than a minute - and the filter by suspect list
SELECT * FROM phone_calls WHERE year = 2024 AND day = 28 AND month = 7 AND duration < 60 AND caller in (
    SELECT phone_number FROM people WHERE id in (686048, 514354, 458378, 395717, 396669, 467400, 449774, 438727) AND license_plate in
(SELECT license_plate FROM bakery_security_logs WHERE year = 2024 AND day = 28 AND month = 7 AND hour = 10 and minute > 15)
);
--this leaves Bruce, Diana and Taylor as Perps and
-- accomplices are
SELECT name FROM people WHERE phone_number IN (
    '(375) 555-8161','(676) 555-6554', '(725) 555-3243'
);
-- James, Philip or Robin

-- Check earliest flight next day
SELECT * FROM flights WHERE year = 2024 AND day = 29 AND month = 7 ORDER BY hour, minute LIMIT 1;

-- id 36, origin - 8, destination - 4
SELECT passport_number FROM passengers WHERE flight_id = 36 AND passport_number IN
(
    SELECT passport_number FROM people WHERE phone_number IN ('(367) 555-5533', '(286) 555-6063', '(770) 555-1861'
    )
);

--update list of perpetrators from people
SELECT * FROM people WHERE passport_number IN (5773159633, 1988161715);
--Taylor or Bruce

-- They escaped to
SELECT city FROM airports WHERE id = 4;

--MASSIVE CROSSEREF BECAUSE IDK HOW TO NARROW

SELECT name FROM people
WHERE phone_number IN
(
    SELECT caller FROM phone_calls WHERE year = 2024 AND day = 28 AND month = 7 AND duration < 60
)
AND license_plate IN
(
    SELECT license_plate
    FROM bakery_security_logs
    WHERE year = 2024
    AND day = 28
    AND month = 7
    AND hour = 10 AND
    minute > 15
    AND minute < 25
    AND activity = 'exit'
)
AND id IN
(
    SELECT person_id FROM bank_accounts WHERE account_number IN
    (
        SELECT account_number FROM atm_transactions WHERE year = 2024
        AND day = 28
        AND month = 7
        AND atm_location = 'Leggett Street'
        AND transaction_type = 'withdraw'
        )
)
AND passport_number IN
(
    SELECT passport_number FROM passengers WHERE flight_id = 36
)
;
-- I GOT YOU BRUCE!!!
-- AND THE ACCOMPLICE IS *drum roll*
SELECT receiver FROM phone_calls WHERE year = 2024 AND day = 28 AND month = 7 AND duration < 60 AND caller = '(367) 555-5533';
SELECT name FROM people WHERE phone_number = '(375) 555-8161';
-- Well isn't this a speaking name
