# Πληροφορίες σχετικά με την εφαρμογή

## Απαιτήσεις της Βάσης Δεδομένων 

1. Κάθε βιβλίο έχει μοναδικό αριθμό id
2. Κάθε χρήστης μπορεί να κάνει αναζήτηση ενός βιβλίου βάσει του τίτλου του, του συγγραφέα του, είδους βιβλίου ή χρονιά δημοσίευσης
3. Ένα βιβλίο μπορεί να έχει πολλούς συγγραφείς
4. Ο χρήστης μπορεί να βάλει ένα βιβλίο στη λίστα των διαβασμένων του και θα υπάρχει ημερομηνία ανάγνωσης του βιβλίου


`login user διάβασε το user authentication και φτιάξε το στο postman....`

## Που κόλησα καθώς ξανάχτιζα την εφαρμογή
- login endpoint έπαιρνα σφάλμα 422 γιατί το έστελνα από Postman χωρίς να επιλέξω form-type το οποίο το είχα βάλει ως παράμετρο στη σχετική συνάρτηση στο routers/auth.py
- Internal Server Error όταν κάνω insert a book και αφού έχω βάλει headers authorization....7:32:20 στο βίντεο
```
[SQL: INSERT INTO books (title, publication_year, owner_id) VALUES (%(title)s, %(publication_year)s, %(owner_id)s) RETURNING books.id]
[parameters: {'title': 'Wisdom of insecurity', 'publication_year': 1956, 'owner_id': None}]
```

## Bugs
- when trying to create user with same email.---internal server error must create an exception

## Που βρίσκομαι...

check code from files or drop tables and start with alembic

### Πίνακες

**Book**
id pk
title
category_id fk
publication_year

**Book-Category**
id pk
category

**Book-Author**
book_id fk
author_id fk


**Author**
id pk
name
date_of_birth
date_of_death

**User**


**Read**
id pk
book_id
user_id
read_date