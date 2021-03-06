import unyt as u

from mc_examples.realistic_workflows.graphene_slitpore.utils import create_system
from mc_examples.realistic_workflows.graphene_slitpore.md_pore.runners import run_gromacs


def main():

    pore_width = 1.5 * u.nm
    n_ion_pairs = 0
    n_water = 183

    filled_pore = create_system(pore_width,
                             n_ion_pairs,
                             n_water,
                             engine='gromacs',
    )

    # Run the MD Simulations
    run_gromacs(filled_pore) 

if __name__ == "__main__":
    main()
