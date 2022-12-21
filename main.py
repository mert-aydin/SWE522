import csv

# number of correct classification of emails
correctResults = 0

# number of feature request classified correctly
feature_emails_detected_correctly = 0

# define the keywords that we want to check for
keywords = ['develop', 'development', 'feature', 'implement']

# open the CSV file and read the emails into a list
with open('Email samples (Feature Requests) - Sheet1.csv', 'r') as csv_file:
    strings_reader = csv.reader(csv_file)
    all_emails = [row[0] for row in strings_reader]

# indices of email data with a feature request mentioned
emails_with_feature_requests = range(0, len(all_emails) - 1)

with open('Email samples (Not Feature Requests) - Sheet1.csv', 'r') as csv_file:
    strings_reader = csv.reader(csv_file)
    all_emails += [row[0] for row in strings_reader]

# iterate over the strings in the sequence
for index, an_email in enumerate(all_emails):
    # initialize a counter to keep track of the number of keywords found in the sequence
    keyword_found = 0
    # check if any of the keywords are in the current string
    if any(keyword in an_email for keyword in keywords):
        # if a keyword is found, increment the keyword count
        keyword_found += 1

    # calculate the certainty value as number of keywords found divided by number of words in an email
    certainty = keyword_found / len(an_email.split()) * 100
    # initialize a flag to keep track of whether the email is about a feature request
    # we detected that 1.65% is the optimal value for classifying an email's topic
    is_feature_request = certainty > 1.65

    # check the value of the flag and print the appropriate message
    if is_feature_request:
        print("%3d. The email is about a feature request with %.2f%% certainty." % ((index + 1), certainty))
        if index in emails_with_feature_requests:
            correctResults += 1
            feature_emails_detected_correctly += 1
        else:
            correctResults -= 1
    else:
        print("%3d. The email is not about a feature request with %.2f%% certainty." % ((index + 1), certainty))
        if index in emails_with_feature_requests:
            correctResults -= 1
        else:
            correctResults += 1

# ratio correct classifications
print("\nPrecision: %.2f%%" % (correctResults / len(all_emails) * 100))
# ratio of number of feature request email detected divided by number of feature request emails
print("Recall: %.2f%%" % (feature_emails_detected_correctly / len(emails_with_feature_requests) * 100))
