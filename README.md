Cogniance QA task
=========

Required libraries to run script:
- unittest
- requests
- json
- random

To run script perform command: 
python checkserver.py -v

Script makes 7 tests:
1) test_gives_list (Checks that the server gives a list of all candidates)
2) test_add_new_candidate (Checks that the server adds new candidate.)
3) test_incorrect_add_data (Checks negative verifications)
4) test_get_one_candidate (Gets the candidate)
5) test_get_one_wrong_candidat (Gets candidate with wrong id)
6) test_get_one_wrong_string_candidate (Gets candidate with wrong id as a string)
7) test_delete_candidate (Checks for correct delete the candidate)

