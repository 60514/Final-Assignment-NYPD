from argparse import ArgumentParser
from pathlib import Path

from analyzer.dictionary import *
from analyzer.works import *
from analyzer.analysis import *
from analyzer.visualization import *

def create_parser():
    parser = ArgumentParser()

    parser.add_argument("--dictionary", type = Path, required = True)

    parser.add_argument("--works", nargs = "+", type = Path, required = True)

    parser.add_argument("--output", type = Path, required = True)

    parser.add_argument("--dictionary-stats", action = "store_true")

    parser.add_argument("--no-words", action = "store_true")

    parser.add_argument("--frequencies", type = int)

    parser.add_argument("--charts", type = Path)

    return parser

def main():
    parser = create_parser()
    args = parser.parse_args()
    d_lines, d_words = read_dictionary(args.dictionary)
    d_stats = calculate_dictionary_statistics(d_lines, d_words)
    works = read_works(args.works)

    with args.output.open("w", encoding = "utf-8") as out:
        if args.dictionary_stats:
            out.write("Dictionary statistics:\n")
            out.write(str(d_stats))
            out.write("\n\n\n")

        for path, (lines, words) in works.items():
            stats = calculate_work_statistics(lines, words)
            out.write(f"{path.name}\n")
            out.write(str(stats))
            out.write("\n\n")

        if len(works) > 1:
            total = calculate_total_statistics(works)
            out.write("TOTAL:\n")
            out.write(str(total))
            out.write("\n\n\n")

        if args.no_words:
            out.write("Unknown words:\n")
            for path, (_, words) in works.items():
                unknown = find_unknown_words(words, d_words)
                out.write(f"{path.name}\n")
                for word, count in unknown:
                    out.write(f"{word}: {count}\n")
            out.write("\n\n\n")

        if args.frequencies:
            frequencies = get_work_frequencies(works, args.frequencies)
            for path, words in frequencies.items():
                out.write(f"Top {args.frequencies} words:\n")
                for word, count in words:
                    out.write(f"{word}: {count}\n")
            out.write("\n\n\n")

    if args.charts:
        similarity = compare_works(works)
        save_similarity_charts(similarity, args.charts)


if __name__ == "__main__":
    main()
