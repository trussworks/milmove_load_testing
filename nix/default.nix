# to install
# nix-env -f nix -i
#
# use
#
# https://ahobson.github.io/nix-package-search/#/search
#
# to find rev for specific package version

let
  pkgs = import <nixpkgs> {};
  inherit (pkgs) buildEnv;
in buildEnv {
  name = "milmove-load-testing-packages";
  paths = [

    (import (builtins.fetchGit {
      # Descriptive name to make the store path easier to identify
      name = "editorconfig-core-c-0.12.1";
      url = "https://github.com/NixOS/nixpkgs/";
      ref = "refs/heads/nixpkgs-unstable";
      rev = "c8ff5bc6f74a2960fab5ae417cd2bb055eab1002";
    }) {}).editorconfig-core-c

    (import (builtins.fetchGit {
      # Descriptive name to make the store path easier to identify
      name = "python3-3.9.6";
      url = "https://github.com/NixOS/nixpkgs/";
      ref = "refs/heads/nixpkgs-unstable";
      rev = "c8ff5bc6f74a2960fab5ae417cd2bb055eab1002";
    }) {}).python3

    (import (builtins.fetchGit {
      # Descriptive name to make the store path easier to identify
      name = "pre-commit-2.13.0";
      url = "https://github.com/NixOS/nixpkgs/";
      ref = "refs/heads/nixpkgs-unstable";
      rev = "f62847d5655a6954fc946e5d9c81424171cc281e";
    }) {}).pre-commit

    (import (builtins.fetchGit {
      # Descriptive name to make the store path easier to identify
      name = "aws-vault-6.3.1";
      url = "https://github.com/NixOS/nixpkgs/";
      ref = "refs/heads/nixpkgs-unstable";
      rev = "253aecf69ed7595aaefabde779aa6449195bebb7";
    }) {}).aws-vault

    (import (builtins.fetchGit {
      # Descriptive name to make the store path easier to identify
      name = "awscli2-2.2.14";
      url = "https://github.com/NixOS/nixpkgs/";
      ref = "refs/heads/nixpkgs-unstable";
      rev = "14b0f20fa1f56438b74100513c9b1f7c072cf789";
    }) {}).awscli2

];
}
