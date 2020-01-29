default_vimrc = "\
set fileencoding=utf-8 fileformat=unix\n\
call plug#begin('~/.vim/plugged')\n\
Plug 'prabirshrestha/async.vim'\n\
Plug 'prabirshrestha/vim-lsp'\n\
Plug 'prabirshrestha/asyncomplete.vim'\n\
Plug 'prabirshrestha/asyncomplete-lsp.vim'\n\
Plug 'mattn/vim-lsp-settings'\n\
Plug 'prabirshrestha/asyncomplete-file.vim'\n\
Plug 'prabirshrestha/asyncomplete-buffer.vim'\n\
Plug 'vim-airline/vim-airline'\n\
Plug 'vim-airline/vim-airline-themes'\n\
Plug 'elzr/vim-json'\n\
Plug 'cohama/lexima.vim'\n\
Plug '{}'\n\
Plug 'cespare/vim-toml'\n\
Plug 'tpope/vim-markdown'\n\
Plug 'kannokanno/previm'\n\
Plug 'tyru/open-browser.vim'\n\
Plug 'ryanoasis/vim-devicons'\n\
Plug 'scrooloose/nerdtree'\n\
Plug 'mattn/emmet-vim'\n\
Plug 'vim/killersheep'\n\
\n\
call plug#end()\n\
\n\
syntax enable\n\
colorscheme {}\n\
set background=dark\n\
\n\
set hlsearch\n\
set cursorline\n\
set cursorcolumn\n\
set number\n\
set foldmethod=marker\n\
set backspace=indent,eol,start\n\
set clipboard^=unnamedplus\n\
set nostartofline\n\
noremap <silent><C-x> :bdelete<CR>\n\
noremap <silent><C-h> :bprevious<CR>\n\
noremap <silent><C-l> :bnext<CR>\n\
set ruler\n\
set noerrorbells\n\
set laststatus={}\n\
set shiftwidth={}\n\
set tabstop={}\n\
set softtabstop={}\n\
set expandtab\n\
set smarttab\n\
set cindent\n\
"

indent_setting_base = "\
augroup {}Indent\n\
  autocmd!\n\
  autocmd FileType {} set tabstop={} softtabstop={} shitwidth={}\n\
augroup END\n\
"
