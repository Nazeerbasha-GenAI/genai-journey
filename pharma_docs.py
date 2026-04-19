# Sample Pharma Documents — Roche Ops Team
# These represent the kind of SOPs and clinical docs your team works with

documents = [
    {
        "id": "SOP-001",
        "title": "Drug Storage and Handling SOP",
        "content": """
        Standard Operating Procedure: Drug Storage and Handling
        Document ID: SOP-001
        Version: 2.1
        Department: Pharma Operations, Roche Bengaluru

        1. PURPOSE
        This SOP defines the requirements for proper storage and handling of 
        pharmaceutical products to maintain quality and safety standards.

        2. TEMPERATURE REQUIREMENTS
        - Cold chain products must be stored between 2-8 degrees Celsius
        - Room temperature products must be stored between 15-25 degrees Celsius
        - Frozen products must be stored at -20 degrees Celsius or below
        - Temperature must be monitored and logged every 4 hours

        3. HANDLING REQUIREMENTS
        - All personnel must wear appropriate PPE when handling drug products
        - Products must never be exposed to direct sunlight
        - Damaged packaging must be immediately reported and quarantined
        - FIFO (First In First Out) principle must always be followed

        4. DOCUMENTATION
        - All storage temperature logs must be maintained for 5 years
        - Any deviation from storage conditions must be reported within 2 hours
        - Monthly audit of storage areas is mandatory
        """
    },
    {
        "id": "SOP-002", 
        "title": "Adverse Event Reporting SOP",
        "content": """
        Standard Operating Procedure: Adverse Event Reporting
        Document ID: SOP-002
        Version: 3.0
        Department: Pharmacovigilance, Roche Bengaluru

        1. PURPOSE
        This SOP defines the process for identifying, documenting, and reporting 
        adverse events related to Roche pharmaceutical products.

        2. DEFINITIONS
        - Adverse Event (AE): Any undesirable medical occurrence in a patient
        - Serious Adverse Event (SAE): AE that results in death, hospitalization,
          or permanent disability
        - Unexpected Adverse Event: AE not listed in current product labeling

        3. REPORTING TIMELINES
        - Fatal or life threatening SAEs must be reported within 7 calendar days
        - All other SAEs must be reported within 15 calendar days
        - Non-serious AEs must be reported within 30 calendar days
        - Follow-up information must be submitted within 15 days of receipt

        4. REPORTING PROCESS
        - All AEs must be logged in the Biovia Nextlab system immediately
        - Medical reviewer must assess causality within 24 hours
        - Regulatory submission must follow ICH E2A guidelines
        - All reports must be reviewed by the pharmacovigilance team lead
        """
    },
    {
        "id": "SOP-003",
        "title": "Clinical Trial Data Management SOP", 
        "content": """
        Standard Operating Procedure: Clinical Trial Data Management
        Document ID: SOP-003
        Version: 1.5
        Department: Clinical Operations, Roche Bengaluru

        1. PURPOSE
        This SOP defines standards for collection, validation, and management 
        of clinical trial data to ensure data integrity and regulatory compliance.

        2. DATA COLLECTION STANDARDS
        - All clinical data must be collected using validated electronic systems
        - Source data must be traceable, legible, and contemporaneous
        - Data entry must be completed within 24 hours of patient visit
        - All data fields must be completed or reasons for missing data documented

        3. DATA VALIDATION
        - Automated edit checks must be applied to all data entries
        - Manual review of flagged data must be completed within 48 hours
        - Query resolution must be documented with audit trail
        - Database lock requires sign-off from data manager and statistician

        4. DATA SECURITY
        - All clinical data must be encrypted at rest and in transit
        - Access to clinical data is role-based and must be approved by IT security
        - Data backup must occur daily with off-site storage
        - Data retention period is 15 years post study completion
        """
    },
    {
        "id": "DRUG-001",
        "title": "Metformin Product Information",
        "content": """
        Product Information Sheet: Metformin Hydrochloride
        Document ID: DRUG-001
        Category: Antidiabetic Agent

        1. DESCRIPTION
        Metformin Hydrochloride is a biguanide class antidiabetic drug used 
        primarily for treatment of type 2 diabetes mellitus.

        2. MECHANISM OF ACTION
        - Reduces hepatic glucose production
        - Improves insulin sensitivity in peripheral tissues
        - Decreases intestinal absorption of glucose
        - Does not cause hypoglycemia when used as monotherapy

        3. DOSAGE AND ADMINISTRATION
        - Initial dose: 500mg twice daily with meals
        - Maintenance dose: 1500-2000mg per day in divided doses
        - Maximum dose: 2550mg per day
        - Must be taken with food to reduce gastrointestinal side effects

        4. CONTRAINDICATIONS
        - Renal impairment with eGFR below 30 mL/min
        - Hepatic impairment
        - Acute or chronic metabolic acidosis
        - History of lactic acidosis

        5. STORAGE
        - Store at room temperature 15-25 degrees Celsius
        - Protect from moisture and light
        - Keep out of reach of children
        - Shelf life: 36 months from manufacture date
        """
    },
    {
        "id": "DRUG-002",
        "title": "Amoxicillin Product Information",
        "content": """
        Product Information Sheet: Amoxicillin Trihydrate
        Document ID: DRUG-002
        Category: Antibiotic — Penicillin class

        1. DESCRIPTION
        Amoxicillin is a broad spectrum penicillin antibiotic effective against 
        both gram-positive and gram-negative bacteria.

        2. MECHANISM OF ACTION
        - Inhibits bacterial cell wall synthesis
        - Binds to penicillin binding proteins
        - Causes cell lysis and bacterial death
        - Bactericidal activity is time-dependent

        3. INDICATIONS
        - Upper and lower respiratory tract infections
        - Urinary tract infections
        - Skin and soft tissue infections
        - H. pylori eradication in combination therapy
        - Dental infections and prophylaxis

        4. DOSAGE
        - Adults: 250-500mg three times daily
        - Children: 25-50mg per kg per day in divided doses
        - Severe infections: up to 1g three times daily
        - Duration: typically 5-10 days depending on infection

        5. STORAGE
        - Store below 25 degrees Celsius
        - Keep in dry conditions away from moisture
        - Oral suspension must be refrigerated after reconstitution
        - Use reconstituted suspension within 14 days
        """
    }
]