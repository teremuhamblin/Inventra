/**
 * ============================
 *   biome.config.js — .github
 * ============================
 */

module.exports = {
  files: {
    include: [
      ".github/**/*"
    ],
    ignore: [
      "node_modules",
      "dist",
      "build"
    ]
  },

  javascript: {
    formatter: {
      quoteStyle: "single",
      trailingCommas: "none",
      indentStyle: "space",
      indentWidth: 2,
      lineWidth: 100
    }
  },

  linter: {
    enabled: true,
    rules: {
      correctness: {
        noUnusedImports: "error",
        noUnusedVariables: "error"
      },
      style: {
        useConst: "error",
        noUselessElse: "error"
      },
      suspicious: {
        noDoubleEquals: "error"
      }
    }
  },

  formatter: {
    enabled: true
  }
};
