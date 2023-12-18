# About

A script to automatically generate a checkout link from a csv of Shopify product IDs.

## Usage

`python gen.py <filename>` to generate a Shopify cart link using the given file.

## File Format

Line 1 contains the BASE url to the site, for example `https://osume.com/`. The script will automatically append `cart/`.

The remaining lines are the variant IDs of the product and their corresponding quantities. Defining quantities is optional, if no quantity is defined, it will default to 1.

## Potential Improvements

- enable pasting of entire product link instead of just the variant id
- validate that the base url of all product links are the same