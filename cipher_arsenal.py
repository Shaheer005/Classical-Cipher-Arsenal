#!/usr/bin/env python3

import sys
import os
import time

from caesar import caesar_encrypt, caesar_decrypt, caesar_break
from vigenere import vigenere_encrypt, vigenere_decrypt, kasiski_examination
from substitution import substitution_encrypt, substitution_decrypt, substitution_break, get_default_substitution_key

if os.name == 'nt':
    os.system('color')

CYAN   = '\033[96m'
GREEN  = '\033[92m'
YELLOW = '\033[93m'
GRAY   = '\033[90m'
WHITE  = '\033[97m'
BOLD   = '\033[1m'
RESET  = '\033[0m'

DIV = GRAY + "___________________________________________________" + RESET

# Each row is exactly 64 chars: A(8) R(8) S(8) E(8) N(10) A(8) L(8) + 6 separators
_ART = [
    " █████╗  ██████╗  ███████╗ ███████╗ ███╗   ██╗  █████╗  ██╗     ",
    "██╔══██╗ ██╔══██╗ ██╔════╝ ██╔════╝ ████╗  ██║ ██╔══██╗ ██║     ",
    "███████║ ██████╔╝ ███████╗ █████╗   ██╔██╗ ██║ ███████║ ██║     ",
    "██╔══██║ ██╔══██╗ ╚════██║ ██╔══╝   ██║╚██╗██║ ██╔══██║ ██║     ",
    "██║  ██║ ██║  ██║ ███████║ ███████╗ ██║ ╚████║ ██║  ██║ ███████╗",
    "╚═╝  ╚═╝ ╚═╝  ╚═╝ ╚══════╝ ╚══════╝ ╚═╝  ╚═══╝ ╚═╝  ╚═╝ ╚══════╝",
]


# ── UI helpers ─────────────────────────────────────────────────────────────

def print_banner():
    W = 68  # content width between ║ bars (art 64 + 2 padding each side)

    border = "╔" + "═" * W + "╗"
    empty  = "║" + " " * W + "║"

    def info(text):
        return "║" + text.center(W) + "║"

    def art_line(row):
        return "║  " + row + "  ║"

    lines = [
        border,
        empty,
        *[art_line(r) for r in _ART],
        empty,
        info("Classical Cipher Toolkit · v1.0.0"),
        info("Information Security | Semester 8E"),
        empty,
        info("Group Delta Members:"),
        info("Shaheer Ahmed (CS221107)"),
        info("Sumeet Jani (CS221109)"),
        info("Ahmed Mubarak (CS221116)"),
        info("Taha Ahmed (CS221029)"),
        empty,
        info("DHA Suffa University"),
        empty,
        "╚" + "═" * W + "╝",
    ]

    print()
    for line in lines:
        print(CYAN + line + RESET)
        time.sleep(0.04)
    print()


def print_main_menu():
    print(DIV)
    print()
    print(BOLD + WHITE + "What would you like to do?" + RESET)
    print(DIV)
    print()
    print(f"  {CYAN}[1]{RESET} Caesar Cipher")
    print(f"  {CYAN}[2]{RESET} Vigenère Cipher")
    print(f"  {CYAN}[3]{RESET} Substitution Cipher")
    print(f"  {CYAN}[4]{RESET} Break a Cipher (Auto Cryptanalysis)")
    print(f"  {CYAN}[5]{RESET} Exit")
    print()
    print(DIV)
    print()


def print_submenu(title):
    print()
    print(BOLD + CYAN + title + RESET)
    print(DIV)
    print()
    print(f"  {CYAN}[1]{RESET} Encrypt a message")
    print(f"  {CYAN}[2]{RESET} Decrypt a message")
    print(f"  {CYAN}[3]{RESET} Back to main menu")
    print()
    print(DIV)
    print()


def print_break_menu():
    print()
    print(BOLD + CYAN + "Break a Cipher (Auto Cryptanalysis)" + RESET)
    print(DIV)
    print()
    print(f"  {CYAN}[1]{RESET} Caesar - Brute Force Attack")
    print(f"  {CYAN}[2]{RESET} Vigenère - Kasiski Examination")
    print(f"  {CYAN}[3]{RESET} Substitution - Frequency Analysis")
    print(f"  {CYAN}[4]{RESET} Back to main menu")
    print()
    print(DIV)
    print()


def what_next_after_encrypt():
    print()
    print(DIV)
    print(BOLD + WHITE + "What next?" + RESET)
    print(DIV)
    print()
    print(f"  {CYAN}[1]{RESET} Encrypt another message")
    print(f"  {CYAN}[2]{RESET} Decrypt a message")
    print(f"  {CYAN}[3]{RESET} Choose a different cipher")
    print(f"  {CYAN}[4]{RESET} Back to main menu")
    print()
    print(DIV)
    print()
    c = input(YELLOW + "> " + RESET + "Enter choice (1-4): ").strip()
    if c == "1": return "encrypt"
    if c == "2": return "decrypt"
    return None  # [3] or [4] → back to main


def what_next_after_decrypt():
    print()
    print(DIV)
    print(BOLD + WHITE + "What next?" + RESET)
    print(DIV)
    print()
    print(f"  {CYAN}[1]{RESET} Encrypt a message")
    print(f"  {CYAN}[2]{RESET} Decrypt another message")
    print(f"  {CYAN}[3]{RESET} Choose a different cipher")
    print(f"  {CYAN}[4]{RESET} Back to main menu")
    print()
    print(DIV)
    print()
    c = input(YELLOW + "> " + RESET + "Enter choice (1-4): ").strip()
    if c == "1": return "encrypt"
    if c == "2": return "decrypt"
    return None


def what_next_after_break():
    print()
    print(DIV)
    print(BOLD + WHITE + "What next?" + RESET)
    print(DIV)
    print()
    print(f"  {CYAN}[1]{RESET} Break another cipher")
    print(f"  {CYAN}[2]{RESET} Choose a different cipher")
    print(f"  {CYAN}[3]{RESET} Back to main menu")
    print()
    print(DIV)
    print()
    c = input(YELLOW + "> " + RESET + "Enter choice (1-3): ").strip()
    if c == "1": return "break"
    return None


def get_shift():
    while True:
        try:
            shift = int(input(YELLOW + "> " + RESET + "Shift (0-25): "))
            if 0 <= shift <= 25:
                return shift
            print(GRAY + "  Please enter a number between 0 and 25." + RESET)
        except ValueError:
            print(GRAY + "  Please enter a valid number." + RESET)


def analyzing():
    print()
    print(GRAY + "  [Analyzing...]" + RESET)
    time.sleep(0.7)
    print()


# ── Cipher menus ───────────────────────────────────────────────────────────

def caesar_menu():
    action = None  # None → show submenu first

    while True:
        if action is None:
            print_submenu("Caesar Cipher")
            c = input(YELLOW + "> " + RESET + "Enter choice (1-3): ").strip()
            if   c == "1": action = "encrypt"
            elif c == "2": action = "decrypt"
            elif c == "3": return
            else:
                print(GRAY + "  Invalid choice." + RESET)
                time.sleep(0.6)
                continue

        if action == "encrypt":
            text  = input(YELLOW + "\n> " + RESET + "Text: ")
            shift = get_shift()
            result = caesar_encrypt(text, shift)
            print(f"\n  {GREEN}→ {WHITE}{result}{RESET}\n")
            action = what_next_after_encrypt()

        elif action == "decrypt":
            text  = input(YELLOW + "\n> " + RESET + "Text: ")
            shift = get_shift()
            result = caesar_decrypt(text, shift)
            print(f"\n  {GREEN}→ {WHITE}{result}{RESET}\n")
            action = what_next_after_decrypt()

        if action is None:
            return


def vigenere_menu():
    action = None

    while True:
        if action is None:
            print_submenu("Vigenère Cipher")
            c = input(YELLOW + "> " + RESET + "Enter choice (1-3): ").strip()
            if   c == "1": action = "encrypt"
            elif c == "2": action = "decrypt"
            elif c == "3": return
            else:
                print(GRAY + "  Invalid choice." + RESET)
                time.sleep(0.6)
                continue

        if action == "encrypt":
            text    = input(YELLOW + "\n> " + RESET + "Text: ")
            keyword = input(YELLOW + "> "  + RESET + "Keyword: ")
            result  = vigenere_encrypt(text, keyword)
            print(f"\n  {GREEN}→ {WHITE}{result}{RESET}\n")
            action = what_next_after_encrypt()

        elif action == "decrypt":
            text    = input(YELLOW + "\n> " + RESET + "Text: ")
            keyword = input(YELLOW + "> "  + RESET + "Keyword: ")
            result  = vigenere_decrypt(text, keyword)
            print(f"\n  {GREEN}→ {WHITE}{result}{RESET}\n")
            action = what_next_after_decrypt()

        if action is None:
            return


def substitution_menu():
    mapping = get_default_substitution_key()
    action  = None

    while True:
        if action is None:
            print_submenu("Substitution Cipher")
            c = input(YELLOW + "> " + RESET + "Enter choice (1-3): ").strip()
            if   c == "1": action = "encrypt"
            elif c == "2": action = "decrypt"
            elif c == "3": return
            else:
                print(GRAY + "  Invalid choice." + RESET)
                time.sleep(0.6)
                continue

        if action == "encrypt":
            text   = input(YELLOW + "\n> " + RESET + "Text: ")
            result = substitution_encrypt(text, mapping)
            print(f"\n  {GREEN}→ {WHITE}{result}{RESET}\n")
            action = what_next_after_encrypt()

        elif action == "decrypt":
            text   = input(YELLOW + "\n> " + RESET + "Text: ")
            result = substitution_decrypt(text, mapping)
            print(f"\n  {GREEN}→ {WHITE}{result}{RESET}\n")
            action = what_next_after_decrypt()

        if action is None:
            return


def break_menu():
    while True:
        print_break_menu()
        c = input(YELLOW + "> " + RESET + "Enter choice (1-4): ").strip()

        if c == "1":
            ciphertext = input(YELLOW + "\n> " + RESET + "Ciphertext: ")
            analyzing()
            results = caesar_break(ciphertext)
            print()
            while True:
                try:
                    shift = int(input(YELLOW + "> " + RESET + "Which shift is correct? (1-25): "))
                    if 1 <= shift <= 25:
                        break
                    print(GRAY + "  Please enter a number between 1 and 25." + RESET)
                except ValueError:
                    print(GRAY + "  Please enter a valid number." + RESET)
            for s, text in results:
                if s == shift:
                    print(f"\n  {GREEN}→ Key:       {WHITE}{shift}{RESET}")
                    print(f"  {GREEN}→ Plaintext: {WHITE}{text}{RESET}\n")
                    break

        elif c == "2":
            ciphertext = input(YELLOW + "\n> " + RESET + "Ciphertext: ")
            analyzing()
            key       = kasiski_examination(ciphertext)
            plaintext = vigenere_decrypt(ciphertext, key)
            print(f"\n  {GREEN}→ Key:       {WHITE}{key}{RESET}")
            print(f"  {GREEN}→ Plaintext: {WHITE}{plaintext}{RESET}\n")

        elif c == "3":
            ciphertext = input(YELLOW + "\n> " + RESET + "Ciphertext: ")
            analyzing()
            plaintext = substitution_break(ciphertext)
            print(f"\n  {GREEN}→ Plaintext: {WHITE}{plaintext}{RESET}\n")

        elif c == "4":
            return

        else:
            print(GRAY + "  Invalid choice." + RESET)
            time.sleep(0.6)
            continue

        if what_next_after_break() is None:
            return


# ── Entry point ────────────────────────────────────────────────────────────

def main():
    print_banner()

    while True:
        print_main_menu()
        choice = input(YELLOW + "> " + RESET + "Enter choice (1-5): ").strip()

        if   choice == "1": caesar_menu()
        elif choice == "2": vigenere_menu()
        elif choice == "3": substitution_menu()
        elif choice == "4": break_menu()
        elif choice == "5":
            print()
            print(GRAY + "  Thank you for using Classical Cipher Arsenal." + RESET)
            print(GRAY + "  Group Delta — Information Security, DHA Suffa University" + RESET)
            print()
            sys.exit(0)
        else:
            print(GRAY + "  Invalid choice. Please enter 1-5." + RESET)
            time.sleep(0.8)


if __name__ == "__main__":
    main()
