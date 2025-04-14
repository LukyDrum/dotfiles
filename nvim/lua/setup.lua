-- Set color scheme
vim.cmd("colorscheme nordfox")

-- Tab size
vim.opt.tabstop = 4
vim.opt.softtabstop = 4
vim.opt.shiftwidth = 4
vim.opt.expandtab = true
vim.opt.smartindent = true

-- Text wrap
vim.opt.wrap = true

-- Enable inlay hints
if vim.lsp.inlay_hint then
	vim.lsp.inlay_hint.enable(true, { 0 })
end

-- Setup bufferline
vim.opt.termguicolors = true

-- Show line numbers
vim.wo.number = true
