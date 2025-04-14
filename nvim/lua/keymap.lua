vim.g.mapleader = " "

-- Save with CTRL-S
vim.keymap.set("n", "<C-s>", ":w<CR>")
vim.keymap.set("i", "<C-s>", "<Esc>:w<CR>")

-- Open file explorer
vim.keymap.set("n", "<leader>e", ":Neotree<CR>")

-- Open symbols outline
vim.keymap.set("n", "<leader>s", ":SymbolsOutline<CR>")

-- Tabs controls
vim.keymap.set("n", "<M-Left>", ":BufferLineCyclePrev<CR>")
vim.keymap.set("n", "<M-Right>", ":BufferLineCycleNext<CR>")
vim.keymap.set("n", "<M-q>", ":bd | bn<CR>")
