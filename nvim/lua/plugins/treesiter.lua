return {
  "nvim-treesitter/nvim-treesitter",
  build = ":TSUpdate",
  opts = function()
    local configs = require("nvim-treesitter.configs")
 
    configs.setup({
      ensure_installed = {
        "c", "lua", "vim", "vimdoc", "elixir", "javascript", "html", "python", "typescript", "rust", "json", "toml", "xml", "c_sharp"
      },
      sync_install = false,
      highlight = { enable = true },
      indent = { enable = true },
    })
  end
}
