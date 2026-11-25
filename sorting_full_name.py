DEFAULT_FULL_NAME = "JED GARRIDO"


def exclude_symbols_and_duplicates(full_name: str) -> list[str]:
    """
    Extracts alphabetic letters from full_name, excludes symbols/spaces/digits,
    and discards duplicate letters (case-insensitive check, keeping original case).
    """
    unique_letters = []
    seen_lower = set()

    for char in full_name:
        if char.isalpha():
            lower_char = char.lower()
            if lower_char not in seen_lower:
                seen_lower.add(lower_char)
                unique_letters.append(char)

    return unique_letters


def bubble_sort_letters(arr: list[str]) -> list[str]:
    """
    Sorts a list of single-character strings alphabetically (case-insensitive)
    using the Bubble Sort algorithm and returns a new sorted list.
    """
    sorted_arr = arr.copy()
    n = len(sorted_arr)

    for i in range(n - 1):
        swapped = False
        for j in range(0, n - 1 - i):
            if sorted_arr[j].lower() > sorted_arr[j + 1].lower():
                sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]
                swapped = True
        if not swapped:
            break

    return sorted_arr


def main() -> None:
    user_input = input(f"Enter your Full Name (press Enter for '{DEFAULT_FULL_NAME}'): ").strip()
    full_name = user_input if user_input else DEFAULT_FULL_NAME

    unsorted_array = exclude_symbols_and_duplicates(full_name)

    if not unsorted_array:
        print("Error: No valid alphabetic letters found after excluding symbols.")
        return

    sorted_array = bubble_sort_letters(unsorted_array)

    print(f"\nFull Name Used: {full_name}")
    print("Unsorted Array (no symbols/duplicates):", unsorted_array)
    print("Sorted Array (Bubble Sort):            ", sorted_array)


if __name__ == "__main__":
    main()