class Quiz:
    manatees = [
        {'name': 'Larry', 'age': 34},
        {'name': 'Gary', 'age': 17},
        {'name': 'Terry', 'age': 84}
        ]
    def example1(manatees):
        for manatee in manatees:
            print (manatee['name'])
    
    def example2(manatees):
        print manatees[0]['name']
        print manatees[0]['age']
    
    def example3(manatees):
        for manatee in manatees:
            for manatee_property in manatee:
                print manatee_property, ": ", manatee[manatee_property]
                
    def example4(manatees):
        oldest_manatee = "No manatess here!"
        for manatee1 in manatees:
            for manatee2 in manatees:
                if manatee1['age'] < manatee2['age']:
                    oldest_manatee = manatee2['name']
                else:
                    oldest_manatee = manatee1['name']
        print oldest_manatee
    
    example1(manatees)
    example2(manatees)
    example3(manatees)
    example4(manatees)
