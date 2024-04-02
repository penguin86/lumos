pkgdatadir = get_option('prefix') / get_option('datadir') / meson.project_name()
moduledir = pkgdatadir / 'lumos'
gnome = import('gnome')

gnome.compile_resources('lumos',
  'lumos.gresource.xml',
  gresource_bundle: true,
  install: true,
  install_dir: pkgdatadir,
)

python = import('python')

conf = configuration_data()
conf.set('PYTHON', python.find_installation('python3').path())
conf.set('VERSION', meson.project_version())
conf.set('localedir', get_option('prefix') / get_option('localedir'))
conf.set('pkgdatadir', pkgdatadir)

configure_file(
  input: 'lumos.in',
  output: 'lumos',
  configuration: conf,
  install: true,
  install_dir: get_option('bindir'),
  install_mode: 'r-xr--r--'
)

lumos_sources = [
  '__init__.py',
  'main.py',
  'window.py',
  'widgets/widgets_loader.py',
  'widgets/time_priority_page.py',
]

install_data(lumos_sources, install_dir: moduledir)
