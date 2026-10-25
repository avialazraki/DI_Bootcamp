
# ============================================
# Week 3 - Day 2 - Daily Challenge
# Pagination System
# ============================================

import math


class Pagination:

    # Step 1 & 2: Initialize pagination
    def __init__(self, items=None, page_size=10):
        self.items = [] if items is None else items

        self.page_size = int(page_size)

        if self.page_size <= 0:
            raise ValueError("Page size must be greater than zero.")

        self.current_idx = 0

        self.total_pages = math.ceil(
            len(self.items) / self.page_size
        )

    # Step 3: Get items on the current page
    def get_visible_items(self):
        start = self.current_idx * self.page_size
        end = start + self.page_size

        return self.items[start:end]

    # Step 4: Navigate to a specific page
    def go_to_page(self, page_num):
        try:
            page_num = int(page_num)
        except (ValueError, TypeError):
            raise ValueError("Page number must be an integer.")

        if page_num < 1 or page_num > self.total_pages:
            raise ValueError(
                f"Page number must be between 1 and {self.total_pages}."
            )

        self.current_idx = page_num - 1
        return self

    # Navigate to the first page
    def first_page(self):
        self.current_idx = 0
        return self

    # Navigate to the last page
    def last_page(self):
        if self.total_pages > 0:
            self.current_idx = self.total_pages - 1

        return self

    # Navigate to the next page
    def next_page(self):
        if self.current_idx < self.total_pages - 1:
            self.current_idx += 1

        return self

    # Navigate to the previous page
    def previous_page(self):
        if self.current_idx > 0:
            self.current_idx -= 1

        return self


# ============================================
# Test the Pagination class
# ============================================

print("Week 3 - Day 2 - Pagination System")

# Create a list of 26 letters
alphabet = list("abcdefghijklmnopqrstuvwxyz")

# Display 5 items per page
pagination = Pagination(alphabet, 5)

print("\nTotal pages:", pagination.total_pages)

print("\nFirst page:")
print(pagination.get_visible_items())

print("\nNext page:")
pagination.next_page()
print(pagination.get_visible_items())

print("\nGo to page 4:")
pagination.go_to_page(4)
print(pagination.get_visible_items())

print("\nLast page:")
pagination.last_page()
print(pagination.get_visible_items())

print("\nPrevious page:")
pagination.previous_page()
print(pagination.get_visible_items())

print("\nMethod chaining:")
pagination.first_page().next_page().next_page()
print(pagination.get_visible_items())

print("\nTest page number as a string:")
pagination.go_to_page("3")
print(pagination.get_visible_items())

print("\nTest invalid page:")
try:
    pagination.go_to_page(100)
except ValueError as error:
    print("Error:", error)

print("\nTest empty list:")
empty_pagination = Pagination()
print(empty_pagination.get_visible_items())
print("Total pages:", empty_pagination.total_pages)
