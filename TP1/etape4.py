import os
import argparse

OUTPUT = "output.txt"
TEMPFILE = "temp.cnf"

def parse_args():  
    '''
    my argumets!!
    '''
    parser = argparse.ArgumentParser(description="Train model.")
    # Path
    parser.add_argument('--path', nargs='?',default='',
                        help='path of the cnf file(base de conaissance)')
    parser.add_argument('--filename', nargs='?',default="test1.cnf",
                    help='nom du fichier cnf de base')
    parser.add_argument('--literal',nargs='?',default="-5 0",
                    help='literal en entrée...')
    
    
    return parser.parse_args()

def neg_lit(literal):
    """
    transformer un literal en sa négation
    """
    if ( "-" in literal ):
        negLit = str( abs (int(literal) ) )
    else:
        negLit = "-" + literal

    return negLit


def clause_to_literals(clause):
    """
    clause: clause ecris en forme cnf :
            exemple 1 -2 0
    """
    lc  = clause.split()
    
    new_list_lit = []
    #plus d'1 seul literal donc on
    #vas faire leurs negation e$
    for i in range(len(lc)-1):
        new_list_lit.append(neg_lit(lc[i]))
    print(new_list_lit)
    return new_list_lit

def add_literal(literal,filename,temporary_file=TEMPFILE):
    """
    
    """ 
    with open(filename,"r") as file :
        contenu = file.readlines()
        # verifier si la variable existe ou pas
        line1 = contenu[0]


        nb_var =int( line1.split()[-2]  )
        nb_clauses = int(line1.split()[-1] )

        #lit_value =  abs(int(literal.split()[0]))
        liste_lit = clause_to_literals(literal)
        print("liste lit:")
        for i in liste_lit:
            print(i)
        for i in liste_lit:
            contenu.append("\n"+i+" 0")
            nb_clauses  = nb_clauses + 1
        #verifier si le liteeral est une nouvelle variable si c'et le cas incrementer le nombre de var
            if i not  in contenu:
                nb_var = nb_var +1
                
        contenu[0] = "p cnf " +  str(nb_var) +  " " +str(nb_clauses) + " \n"
        
    with open(temporary_file,"w") as file:
        for i in contenu:
            file.writelines(i)
        
def est_satisfaisable(output=OUTPUT):
    """
    output: le nom fichier en sortie  apres execution de ubcsat
    """
    with open(output,"r") as file:
        line = file.read()
        if "# Solution found for " in line:
            return True 
        elif("# No Solution found" in line):
            return False
def exec_obcsat(filename,out=OUTPUT):
    os.system(f"./ubcsat -alg  saps -i {filename} -solve > {out}")

def main():
    
    args = parse_args()
    file_bc = args.path  + args.filename
    exec_obcsat(file_bc)
    if est_satisfaisable():
        add_literal(args.literal,file_bc)
        exec_obcsat(TEMPFILE)
        if not est_satisfaisable() :
            print(f"la base de conaissance {args.filename} infére {args.literal}")
        else:
            print(f"la base de conaissance {args.filename} n\'infére pas {args.literal}")
    
        os.remove(TEMPFILE)
        os.remove(OUTPUT)    
        
    else:
        print(f"ERREUR BC {file_bc} Non satisfaisable, veuillez en choisir une autre! ")
        
    
    
if __name__=="__main__":
   main() 
