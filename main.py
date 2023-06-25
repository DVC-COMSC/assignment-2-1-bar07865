def main():
    
    males = int(input("Enter the number of males:"))
    females = int(input("Enter number of females:"))
    total = males + females 
    m_perc = (males / total) * 100
    f_perc = (females / total) * 100

    print("Total number of students: \t ", total)
    print("The number of males and females: \t ", males , females )
    print("Percentage of males and females: \t ", m_perc,"%", f_perc,"%" )
    return m_perc, f_perc


if __name__ == '__main__':
    main()
