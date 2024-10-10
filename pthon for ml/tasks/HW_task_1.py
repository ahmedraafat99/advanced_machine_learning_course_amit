def validate_email(email):
    if email.count('@') !=1  or '.' not in email.split('@')[1]:
        return"invalid email"
    
    username=email.split('@')[0]
    
    domain=email.split('@')[1].rsplit('.',1)[0]
    
    if email.endswith('.com'):
        domain_type="Commercial Domain"
    elif email.endswith('.edu'):
        domain_type="Educational Domain"
    else:
        domain_type="other domain"
    
    return{
        
        'username'  :username,
        'domain'     :domain,
        'domain_type':domain_type
    }            
    
email= "Amit_ml@gmail.edu"
print(validate_email(email))