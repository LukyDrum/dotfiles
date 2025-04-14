return {
    'akinsho/bufferline.nvim',
    version = "*",
    dependencies = 'nvim-tree/nvim-web-devicons',
    opts = {
        options = {
            seperator_style = "slope",
            diagnostics = "nvim_lsp",
            offsets = {
                {
                    filetype = "NeoTree",
                    text = "File Explorer",
                    highlight = "Directory",
                    separator = true,
                },
            }
        }
    }
}
