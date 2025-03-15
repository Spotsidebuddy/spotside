import csv
import sys


def main():

    # Check for command-line usage
    if len(sys.argv) != 3:
        print("Usage: python dna.py <database> <sequence>")
        sys.exit()

    # Read database file into a variable
    data = {}

    with open(sys.argv[1], mode="r") as database:
        reader = csv.DictReader(database)
        for row in reader:
            name = row.pop("name")
            data[name] = {key: int(value) for key, value in row.items()}

    # Read DNA sequence file into a variable
    with open(sys.argv[2]) as sequence:
        seq = sequence.read()

    # Find longest match of each STR in DNA sequence
    strs = list(data.values())[0].keys()
    longest_matches = {}
    for item in strs:
        longest_matches[item] = longest_match(seq, item)

    # Check database for matching profiles
    for person, str_counts in data.items():
        if all(str_counts[s] == longest_matches[s] for s in longest_matches):
            print(person)
            return
    else:
        print("No matches")
        return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1
            
            # If there is no match in the substring
            else:
                break
        
        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in sequence, return longest run found
    return longest_run

if __name__ == '__main__':
    main()
