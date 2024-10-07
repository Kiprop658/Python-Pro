def main():

    user_input = input("Please enter a list of names separated by commas: ")
    names = [name.strip() for name in user_input.split(',')]
    unique_names = list(set(names))
    
    unique_names.sort()
    print("\nSorted list of unique names:")
    for name in unique_names:
        print(name)
    print(f"\nTotal number of unique names entered: {len(unique_names)}")

if __name__ == "__main__":
    main()
