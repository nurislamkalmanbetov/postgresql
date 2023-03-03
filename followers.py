logins = (
    'Atai','Sultan','Adinai','Ermek',
    'Aslan','Liazat','Salavat','Daniyar',
    'Bolot','Alymbek','Joomart','Aibek',
    'Aibek','Konstantin','Oliver','Jake',
    'Noah','James','Jack','Connor','Liam',
    'John','Harry','Callum','Mason','Robert',
    'Jacob','Jacob','Jacob','Michael','Charlie',
    'Kyle','William','William','Thomas','Joe',
    'Ethan','David','George','Reece','Michael',
    'Richard','Oscar','Rhys','Alexander','Joseph',
    'James','Charlie','James','Charles','William',
    'Damian','Daniel','Thomas','Amelia','Margaret',
    'Emma','Mary','Olivia','Samantha','Olivia',
    'Patricia','Isla','Bethany','Sophia',
    'Jennifer','Emily','Elizabeth','Isabella',
    'Elizabeth','Poppy','Joanne','Ava','Linda',
    'Ava','Megan','Mia','Barbara','Isabella','Victoria',
    'Emily','Susan','Jessica','Lauren','Abigail',
    'Margaret','Lily','Michelle','Madison','Jessica',
    'Sophie','Tracy','Charlotte','Sarah', 'qwerty',
    'test_user','test_test','user123','user_user', 'bzzzz',
)


professions = (
    'Cloud Architect',
    'Cloud Consultant',
    'Cloud Product and Project Manager',
    'Cloud Services Developer',
    'Cloud Software and Network Engineer',
    'Cloud System Administrator',
    'Cloud System Engineer',
    'Computer and Information Research Scientist',
    'Computer and Information Systems Manager',
    'Computer Network Architect',
    'Computer Systems Analyst',
    'Computer Systems Manager',
    'IT Analyst',
    'IT Coordinator',
    'Network Administrator',
    'Network Architect',
    'Network and Computer Systems Administrator',
    'Network Engineer',
    'Network Systems Administrator',
    'Senior Network Architect',
    'Senior Network Engineer',
    'Senior Network System Administrator',
    'Telecommunications Specialist',
    'Customer Support Administrator',
    'Customer Support Specialist',
    'Desktop Support Manager',
    'Desktop Support Specialist',
    'Help Desk Specialist',
    'Help Desk Technician',
    'IT Support Manager',
    'IT Support Specialist',
    'IT Systems Administrator',
    'Senior Support Specialist',
    'Senior System Administrator',
    'Support Specialist',
    'Systems Administrator',
    'Technical Specialist',
    'Technical Support Engineer',
    'Technical Support Specialist',
    'Data Center Support Specialist',
    'Data Quality Manager',
    'Database Administrator',
    'Senior Database Administrator',
    'Application Support Analyst',
    'Senior System Analyst',
    'Systems Analyst',
    'Systems Designer',
    'Chief Information Officer (CIO)',
    'Chief Technology Officer (CTO)',
    'Director of Technology',
    'IT Director',
    'IT Manager',
    'Management Information Systems Director',
    'Technical Operations Officer',
    'Information Security',
    'Security Specialist',
    'Senior Security Specialist',
    'Application Developer',
    'Applications Engineer',
    'Associate Developer',
    'Computer Programmer',
    'Developer',
    'Java Developer',
    'Junior Software Engineer',
    '.NET Developer',
    'Programmer',
    'Programmer Analyst',
    'Senior Applications Engineer',
    'Senior Programmer',
    'Senior Programmer Analyst',
    'Senior Software Engineer',
    'Senior System Architect',
    'Senior System Designer',
    'Senior Systems Software Engineer',
    'Software Architect',
    'Software Developer',
    'Software Engineer',
    'Software Quality Assurance Analyst',
    'System Architect',
    'Systems Software Engineer',
    'Front End Developer',
    'Senior Web Administrator',
    'Senior Web Developer',
    'Web Administrator',
    'Web Developer',
    'Webmaster'
)

pswd_symbols = ('!', '@', '#', '$', '%', '&')

streets = (
    "Main Street",
    "Oak Street",
    "Park Avenue",
    "Maple Avenue",
    "Elm Street",
    "Cedar Lane",
    "Broadway",
    "Pine Street",
    "Hillside Avenue",
    "Willow Street",
    "Church Street",
    "Washington Avenue",
    "Highland Avenue",
    "River Road",
    "Chestnut Street",
    "Lincoln Avenue",
    "Cherry Lane",
    "Prospect Street",
    "Smith Street",
    "Meadow Lane"
)

countries = (
    "United States",
    "Canada",
    "Mexico",
    "Brazil",
    "Argentina",
    "United Kingdom",
    "Germany",
    "France",
    "Spain",
    "Italy",
    "Russia",
    "China",
    "Japan",
    "India",
    "Australia",
    "South Africa",
    "Egypt",
    "Nigeria",
    "Kenya",
    "Morocco"
)


import psycopg2
import random as rd

def connect(db_name: str, user: str, password: str, host: str = 'localhost'):
    conn = psycopg2.connect(
        dbname=db_name,
        user=user,
        password=password,
        host=host
    )
    return conn



def generate_password():
    password_list = []
    
    for _ in range(5000):
        password = ''
        for _ in range(rd.randint(8, 16)):
            password += rd.choice(pswd_symbols)
        password_list.append(password)

    return password_list

def generate_email(logins: list) -> list:
    domen = ("@gmail.com", "@mail.ru", "@yandex.kz", "@yandex.kg", "@bk.ru")
    email_list = []

    for name in logins:
        email_list.append(name+rd.choice(domen))
    
    return email_list


def generate_phone() -> list:
    codes = ("77", "70")
    phone_list = []
    
    for _ in range(5000):
        number = '+7'+ rd.choice(codes) + str(rd.randint(10000000, 99999999))
        phone_list.append(number)

    return phone_list


def generate_streets(streets: list) -> list:
    street_list = []
    for _ in range(5000):
        address = rd.choice(streets)+ ' ' + str(rd.randint(1, 150))
        street_list.append(address)
    return street_list


def create_table(conn: object) -> None:
    query = """
    CREATE TABLE users(
        id SERIAL PRIMARY KEY,
        login VARCHAR(50) NOT NULL,
        password VARCHAR(50) NOT NULL,
        email VARCHAR(50) NOT NULL,
        phone VARCHAR(50) NOT NULL,
        country VARCHAR(50) NOT NULL,
        address VARCHAR(50) NOT NULL,
        profession VARCHAR(50) NOT NULL,
        followers INT NOT NULL
    );
    """
    cursor = conn.cursor()
    cursor.execute(query)
    print("Table created success")
    conn.commit()


def inser(conn: object, logins: list , passwords: list, emails: list, 
            phones: list, countries: list, addresses: list, professions: list):

    query = """INSERT INTO users(
        login, password, email, phone, country, address, profession, followers
    )
    VALUES """

    # (),
    # (),
    # ()

    for _ in range(10000):
        query += f"""(
        '{rd.choice(logins)}',
        '{rd.choice(passwords)}',
        '{rd.choice(emails)}',
        '{rd.choice(phones)}',
        '{rd.choice(countries)}',
        '{rd.choice(addresses)}',
        '{rd.choice(professions)}',
        {rd.randint(1, 10000000)}
        ),"""
    
    query = query[:-1] + ';'
    cursor = conn.cursor()
    cursor.execute(query)
    print("ISERT success")
    conn.commit()
    cursor.close()
    conn.close()


logins = logins
passwords = generate_password()
emails = generate_email(logins)
phones = generate_phone()
countries = countries
addresses = generate_streets(streets)
professions = professions



# db_name = input("Введите имя Базы Данных: \n >>> ")
# user = input("Введите имя пользователя Базы Данных: \n >>> ")
# password = input("Введите пароль от Базы Данных: \n >>> ")


db_name = 'programmers_db'
user = 'postgres'
password = 'qwerty123'

conn = connect(
    db_name=db_name,
    user=user,
    password=password
)

create_table(conn=conn)

inser(
    conn=conn,
    logins=logins,
    passwords=passwords,
    emails=emails,
    phones=phones,
    countries=countries,
    addresses=addresses,
    professions=professions
)